# Github-Aggregator

## Features to be introduced

- [x] Introduce dark border around the result table
- [x] Button Feature to download the CSV file of the results
- [x] Use github api token for github authentication process
- [ ] Proper implementation of Input, output, GET, POST method so that client can input the repository name
- [x] Amend the title such that the Repository name is visible in it
- [x] Return the relevant response if the repository does not exist

## Bugs to fix

- [x] View the number of unique contributors in case the data does not exist in the MySQL database
- [x] Total Number of contributions comes out as 30 irrespective of the repository
- [x] Pass the repo name to download csv function such that it returns the table result accordingly

## Time Complexity

- [ ] Reduce latency, time taken to display result table takes too long even if the data exists in the MySQL database

## Security issues

- [x] Mask the sensitive info (passwords, token keys) present in the files using environmental variables

## Testing

- [ ] Test the Flask application using unittest or pytest

## Challenges Faced

* Latency issues when querying data from the MySQL database
* API rate limit per hour exceeding for repositories that have high number of commits
