from flask import Flask, jsonify
import requests
import json
from collections import defaultdict
import mysql.connector

app = Flask(__name__)

# Define database connection parameters
db_config = {
    'user': 'Qaiser',
    'password': 'Sayedali@732',
    'host': '127.0.0.1',
    'database': 'github_aggregator'
}

# Create database connection
db_conn = mysql.connector.connect(**db_config)
db_cursor = db_conn.cursor()


@app.route('/contributors')
def contributors():
    repo_name = 'hashicorp/consul'
    url = f"https://api.github.com/repos/{repo_name}/commits"
    headers = {'Accept': 'application/vnd.github.v3+json'}

    # Send GET request to GitHub API to fetch all commits for the repository
    response = requests.get(url, headers=headers)
    data = response.json()

    # Initialize dictionary to store total contributions and unique contributors for each domain
    domain_stats = defaultdict(lambda: {'total_contributions': 0, 'unique_contributors': set()})

    # Iterate over each commit and extract domain from email
    for commit in data:
        email = commit['commit']['author']['email']
        domain = email.split('@')[-1]
        domain_stats[domain]['total_contributions'] += 1
        domain_stats[domain]['unique_contributors'].add(commit['commit']['author']['name'])

    # Convert defaultdict to regular dictionary and sort by total contributions
    domain_stats = dict(sorted(domain_stats.items(), key=lambda x: x[1]['total_contributions'], reverse=True))

    # Store data in MySQL database
    for domain, stats in domain_stats.items():
        total_contributions = stats['total_contributions']
        unique_contributors = len(stats['unique_contributors'])
        insert_query = f"INSERT INTO contributors (repo_name, domain, total_contributions, unique_contributors) VALUES ('{repo_name}', '{domain}', {total_contributions}, {unique_contributors})"
        db_cursor.execute(insert_query)
        db_conn.commit()

    # Convert dictionary to JSON and return as response
    for domain, stats in domain_stats.items():
        stats['unique_contributors'] = len(list(stats['unique_contributors']))

    # Return JSON response
    return json.dumps(domain_stats)
    #return jsonify(domain_stats)

if __name__ == '__main__':
    app.run(debug=True)