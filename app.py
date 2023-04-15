from flask import Flask, jsonify, request
from github import Github
import mysql.connector

app = Flask(__name__)

@app.route('/contributors', methods=['GET'])
def get_contributors():
    repo_name = request.args.get('hashicorp') # get repository name from query parameter
    g = Github() # initialize PyGithub with your credentials or use anonymously
    repo = g.get_repo(repo_name)
    contributors = {}
    branches = repo.get_branches()
    for branch in branches:
        commits = repo.get_commits(sha=branch.name)
        for commit in commits:
            author = commit.author
            if author is None:
                continue
            if author.login not in contributors:
                contributors[author.login] = {"company": None, "commits": 1}
            else:
                contributors[author.login]["commits"] += 1

            for email in author.emails:
                if email.endswith("@example.com"):
                    contributors[author.login]["company"] = "Example Inc."
                    break

    # Calculate total contributions and unique contributors per company
    companies = {}
    for contributor in contributors.values():
        company = contributor["company"]
        if company is None:
            continue
        if company not in companies:
            companies[company] = {"total_contributions": 0, "unique_contributors": 0}
        companies[company]["total_contributions"] += contributor["commits"]
        companies[company]["unique_contributors"] += 1

    # Store sorted contributor information in MySQL database
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='Qaiser',
            password='Sayedali@732',
            database='github_aggregator'
        )
        cursor = connection.cursor()

        # Create table if it does not exist
        cursor.execute("CREATE TABLE IF NOT EXISTS contributors (company VARCHAR(255), total_contributions INT, unique_contributors INT)")

        # Clear any previous data
        cursor.execute("TRUNCATE TABLE contributors")

        # Insert new data
        for company, data in companies.items():
            cursor.execute("INSERT INTO contributors (company, total_contributions, unique_contributors) VALUES (%s, %s, %s)",
                           (company, data["total_contributions"], data["unique_contributors"]))

        # Commit changes
        connection.commit()

        # Close cursor and connection
        cursor.close()
        connection.close()

    except Exception as e:
        print("Error storing data in MySQL database: ", e)

    return jsonify(companies)

if __name__ == '__main__':
    app.run(debug=True)
