# Github-Aggregator

## Features to be introduced

- [x] Introduce dark border around the result table
- [x] Button Feature to download the CSV file of the results
- [x] Use github api token for github authentication process
- [ ] Create the HTML page for the user to enter the name of the repository
- [ ] Take the user provided input and do the checks related to the repository, return the response accordingly
- [ ] Make the changes to the python code such that repository name is passed down to the donwload csv function and it returns the table result according to the repository name given as input
- [x] Amend the title such that the Repository name is visible in it
- [x] Return the relevant response if the repository does not exist

## Bugs to fix

- [x] View the number of unique contributors in case the data does not exist in the MySQL database
- [x] Total Number of contributions comes out as 30 irrespective of the repository

## Time Complexity

- [ ] Reduce latency, time taken to display result table takes too long even if the data exists in the MySQL database

## Security issues

- [x] Mask the sensitive info (passwords, token keys) present in the files using environmental variables
