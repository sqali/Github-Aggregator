# GitHub Aggregator

GitHub Aggregator is a web application built with Flask that collects commit data from a specific GitHub repository and provides insights about the contributors based on their email domains. It helps you understand the distribution of contributions across different domains and the unique contributors involved in a repository.

## Features

- Collects commit data from a specified GitHub repository.
- Analyzes the email domains of contributors to identify the distribution of contributions.
- Calculates the total contributions and unique contributors for each domain.
- Stores the results in a MySQL database for future reference.
- Provides a web interface to view the aggregated data.
- Generates a downloadable CSV report containing the aggregated data.

## Installation

To use GitHub Aggregator, follow these steps:

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/github-aggregator.git
   cd github-aggregator```
   
2. Install the dependencies

   ```pip install -r requirements.txt```
   
3. Set up the database:

- Make sure you have MySQL installed and running.
- Update the db_config variable in the app.py file with your MySQL connection details.

4. Configure the GitHub token:

- Create a personal access token on GitHub with the necessary permissions to access the repository's commit data.
- Set the TOKEN environment variable with your GitHub token.

5. Run the application:

  ```python app.py```
