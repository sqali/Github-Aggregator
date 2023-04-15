import mysql.connector
from flask import Flask, jsonify
from github import Github

app = Flask(__name__)

# connect to MySQL database
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="Qaiser",
  password="Sayedali@732",
  database="github_aggregator"
)

# create a cursor to execute SQL queries
mycursor = mydb.cursor()

# create table to store the data
mycursor.execute("CREATE TABLE IF NOT EXISTS contributions (id INT AUTO_INCREMENT PRIMARY KEY, company VARCHAR(255), contributions INT, contributors INT)")

@app.route('//github.com/hashicorp')
def get_contributions(repo):
    # initialize GitHub API object
    g = Github()

    # get the repository object
    repo = g.get_repo(repo)

    # get all the branches in the repository
    branches = repo.get_branches()

    # create an empty dictionary to store the results
    result = {}

    # iterate over each branch
    for branch in branches:
        # get the commit object for the head of the branch
        commit = repo.get_commit(sha=branch.commit.sha)

        # get the list of contributors for the commit
        contributors = commit.get_contributors()

        # iterate over each contributor and add to the dictionary
        for contributor in contributors:
            # get the company name from the contributor's profile
            company = contributor.company

            # if the company is not set, set it to "Unknown"
            if not company:
                company = "Unknown"

            # if the company is already in the dictionary, add to the contributions and contributors count
            if company in result:
                result[company]["contributions"] += 1
                if contributor.login not in result[company]["contributors"]:
                    result[company]["contributors"].append(contributor.login)
            # if the company is not in the dictionary, create a new entry
            else:
                result[company] = {}
                result[company]["contributions"] = 1
                result[company]["contributors"] = [contributor.login]

    # iterate over the dictionary and insert data into the MySQL database
    for company in result:
        contributions = result[company]["contributions"]
        contributors = len(result[company]["contributors"])
        sql = "INSERT INTO contributions (company, contributions, contributors) VALUES (%s, %s, %s)"
        val = (company, contributions, contributors)
        mycursor.execute(sql, val)

    # commit changes to the database
    mydb.commit()

    # format the result as a dictionary
    response = {}
    for company in result:
        contributions = result[company]["contributions"]
        contributors = len(result[company]["contributors"])
        response[company] = f"{contributions}: {contributors}"

    # return the result as a JSON response
    return jsonify(response)

if __name__ == '__main__':
    app.run()
