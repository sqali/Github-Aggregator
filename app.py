from flask import Flask, jsonify, make_response, Response, render_template
import requests
import json
from collections import defaultdict
import mysql.connector
import csv
import re
from dotenv import load_dotenv
import os
load_dotenv()

db_password = os.getenv('DB_PASSWORD')
github_token = os.getenv("TOKEN")

app = Flask(__name__)


# Define database connection parameters
db_config = {
    'user': 'Qaiser',
    'password': db_password,
    'host': '127.0.0.1',
    'database': 'github_aggregator'
}

# Create database connection
db_conn = mysql.connector.connect(**db_config)
db_cursor = db_conn.cursor()
repo_name = "scipy/scipy-cookbook"

def get_next_page(links):
    # Extracts the URL for the next page from the "Link" header
    parts = links.split(',')
    for part in parts:
        section = part.split(';')
        if 'rel="next"' in section[1]:
            return section[0].strip()[1:-1]  # Remove '<' and '>' from the URL
    return None


@app.route('/')
def contributors():
    url = f"https://api.github.com/repos/{repo_name}/commits"
    headers = {'Accept': 'application/vnd.github.v3+json', 'Authorization': f'Bearer {github_token}'}

    # Send GET request to GitHub API to fetch all commits for the repository
    response = requests.get(url, headers=headers)

    if response.status_code == 404:
        return render_template("not_found.html")

    data = response.json()

    # Initialize dictionary to store total contributions and unique contributors for each domain
    domain_stats = defaultdict(lambda: {'total_contributions': 0, 'unique_contributors': set()})

    # Iterate over each commit and extract domain from email
    for commit in data:
        email = commit['commit']['author']['email']
        domain = email.split('@')[-1]
        domain_stats[domain]['total_contributions'] += 1
        domain_stats[domain]['unique_contributors'].add(commit['commit']['author']['name'])

    # Iterating over all the pages of commits
    if 'Link' in response.headers:
        links = response.headers['Link']
        next_page = get_next_page(links)
        while next_page:
            response = requests.get(next_page, headers=headers)
            data = response.json()
            for commit in data:
                email = commit['commit']['author']['email']
                domain = email.split('@')[-1]
                domain_stats[domain]['total_contributions'] += 1
                domain_stats[domain]['unique_contributors'].add(commit['commit']['author']['name'])
            if 'Link' in response.headers:
                links = response.headers['Link']
                next_page = get_next_page(links)
            else:
                break

    # Convert defaultdict to regular dictionary and sort by total contributions
    domain_stats = dict(sorted(domain_stats.items(), key=lambda x: x[1]['total_contributions'], reverse=True))

    # Store data in MySQL database
    select_query = f"SELECT COUNT(*) FROM contributors WHERE repo_name = '{repo_name}' AND domain = '{domain}'"
    db_cursor.execute(select_query)
    result = db_cursor.fetchone()
    record_count = result[0]

    if record_count > 0:
        # Data already exists in the database, retrieve and return the result
        select_query = f"SELECT domain, total_contributions, unique_contributors FROM contributors WHERE repo_name = '{repo_name}'"
        db_cursor.execute(select_query)
        db_results = db_cursor.fetchall()

        # Prepare result dictionary
        result_dict = {}
        for row in db_results:
            domain = row[0]
            total_contributions = row[1]
            unique_contributors = row[2]
            result_dict[domain] = {'total_contributions': total_contributions, 'unique_contributors': unique_contributors}

        repository = re.match(r"([^/]*)", repo_name).group(1)
        return render_template("contributors.html", repository= repository, domain_stats=result_dict)
    
    else:
        # Data doesn't exist in the database, store the data
        for domain, stats in domain_stats.items():
            total_contributions = stats['total_contributions']
            unique_contributors = len(stats['unique_contributors'])
            insert_query = f"INSERT INTO contributors (repo_name, domain, total_contributions, unique_contributors) VALUES ('{repo_name}', '{domain}', {total_contributions}, {unique_contributors})"
            db_cursor.execute(insert_query)
        db_conn.commit()

        # Return JSON response
        repository = re.match(r"([^/]*)", repo_name).group(1)
        return render_template("contributors.html", repository= repository, domain_stats=domain_stats)

    
@app.route('/download_csv')
def download_csv():
    select_query = f"SELECT domain, total_contributions, unique_contributors FROM contributors WHERE repo_name = '{repo_name}'"
    db_cursor.execute(select_query)
    db_results = db_cursor.fetchall()

    # Prepare the CSV data
    csv_data = []
    csv_data.append(['Domain', 'Total Contributions', 'Unique Contributors'])
    for row in db_results:
        domain = row[0]
        total_contributions = row[1]
        unique_contributors = row[2]
        csv_data.append([domain, total_contributions, unique_contributors])

    # Create a response object with CSV data
    csv_response = make_response('')
    csv_response.headers['Content-Disposition'] = 'attachment; filename=result.csv'
    csv_response.headers['Content-Type'] = 'text/csv'

    # Write CSV data to the response
    stream = csv_response.stream
    writer = csv.writer(stream)
    writer.writerows(csv_data)

    return csv_response

if __name__ == '__main__':
    app.run(debug=True)