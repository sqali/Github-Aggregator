# Github-Aggregator

Github-Aggregator is a Flask web application that aggregates commit data from a repository using the GitHub REST API. It provides a user-friendly interface to input repository details and retrieve insightful information about the commits.

## Features

### User Interface Enhancements

- **Introduce a dark border around the result table:** Implemented a visual enhancement by adding a dark border around the result table to improve readability.

- **Button Feature to download the CSV file of the results:** Added a button that allows users to download the result table as a CSV file for further analysis.

- **View the load button for the number of pages extracted:** Planned feature to display the progress of data extraction by showing the number of pages extracted and the total number of pages.

- **Amend the title such that the Repository name is visible:** Modified the title to include the name of the repository, providing better context to users.

### Data Extraction and Analysis

- **Use GitHub API token for GitHub authentication process:** Enhanced security by integrating GitHub API token authentication, ensuring secure access to repository data.

- **Proper implementation of Input, Output, GET, POST method:** In progress. This feature will enable users to input the repository name and interact with the application using appropriate HTTP methods.

- **Return relevant response if the repository does not exist:** Implemented an appropriate response when a non-existent repository is requested.

### User Interaction and Collaboration

- **User Authentication and Authorization:** Allow users to create accounts, log in, and access personalized features such as saving favorite repositories, creating custom reports, or sharing insights with other users.

- **Real-time Updates:** Integrate websockets or a messaging queue system to provide real-time updates of commit activities, enabling users to see live notifications, updates, or visualizations as commits happen.

- **Advanced Data Visualization:** Enhance the data visualization capabilities by incorporating more advanced charting libraries or interactive visualizations like D3.js or Plotly. Explore options for creating meaningful insights and trend analysis from commit data.

- **Collaboration and Social Features:** Enable users to collaborate on repositories, comment on commits, and share insights with others. Implement features like pull request tracking, code review functionality, and social sharing options to foster a vibrant community around the project.

### Advanced Features

- **Integration with CI/CD Pipelines:** Integrate your project with popular CI/CD (Continuous Integration/Continuous Deployment) platforms like Jenkins, CircleCI, or GitHub Actions. This allows automated testing, build, and deployment processes triggered by commit activities, providing a seamless development workflow.

- **Machine Learning and Predictive Analysis:** Apply machine learning algorithms to analyze commit patterns, predict code quality issues, or identify potential bugs. This could involve using techniques like anomaly detection, sentiment analysis on commit messages, or code complexity analysis.

- **Advanced Search and Filtering:** Improve search functionality to allow users to search for commits based on various criteria such as commit message, author, date range, or specific code changes. Implement advanced filtering options to refine search results and provide a more focused analysis.

- **Support for Multiple Version Control Systems:** Extend the application's capabilities to support other version control systems like GitLab or Bitbucket. This allows users to analyze commit data from different platforms and repositories.

- **Integration with External APIs:** Explore integrating with other APIs, such as project management tools (Jira, Trello) or code quality analysis tools (SonarQube), to enrich the commit analysis process.

### Bug Fixes

- **View the number of unique contributors in case the data does not exist in the MySQL database:** Resolved an issue where the count of unique contributors was not displayed when data was missing from the MySQL database.

- **Total Number of contributions comes out as 30 irrespective of the repository:** Fixed an issue where the total number of contributions was consistently displayed as 30 regardless of the repository.

- **Pass the repo name to the download CSV function:** Updated the download CSV function to correctly return the table result based on the repository name.

### Database Normalization & MySQL script

- **Design your database schema to apply normalization techniques in MySQL Workbench:** Work in progress. This section will guide you through designing a database schema and applying normalization techniques using MySQL Workbench.

- **Generate the MySQL script based on the database schema:** Once the database schema is designed, this section will provide guidance on generating the MySQL script for creating the necessary tables and relationships.

### Latency

- **Optimize the time taken to retrieve the results from the MySQL database:** This section will explore strategies and optimizations to improve the retrieval time of results from the MySQL database, addressing latency issues.

- **Caching to reduce latency time:** Implemented caching functionality to reduce latency and improve performance. Cached results will be served for subsequent requests, minimizing database queries.

### Security issues

- **Mask the sensitive info using environmental variables:** Improved security by storing sensitive information such as passwords and token keys as environmental variables, preventing them from being exposed in the codebase.

### Testing

- **Test the Flask application using unittest or pytest:** This section will cover how to perform testing on the Flask application using either the unittest or pytest framework to ensure the functionality of the project.

## Installation and Usage

1. Clone the repository: `git clone https://github.com/your-username/Github-Aggregator.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Set up the necessary environment variables for security: `export FLASK_APP=app.py` and `export FLASK_ENV=development`
4. Run the Flask application: `python -u location-of-file`
5. Access the application through your web browser: `http://localhost:5000`

Feel free to explore the different features and contribute to the project by fixing bugs or adding new functionalities!
