This repository analyzes data from the budget_data and election_data csv files and exports the results of both analysis to two separate text files.

The repository contains two folders: PyBank and PyPoll. In the PyBank analysis, the csv file budget_data holds profit/losses data over a number of months. The python script "main.py" has been used to analyze the data to produce insights including: Total number of months in dataset, sum of profit/Losses, the average change in profit/losses, the greatest increase in profits, and the greatest decrease in profits.

The Pypoll analysis folder holds the election_data csv file which contains the ballot, county and candidate information from a recent election. The main.py script has been used to analyze this data to produce a text file containing insights such as: total number of votes cast, percentage of votes each candidate won, total number of votes each candidate won, winner of the election based on popular vote.

The file structure for both PyBank and PyPoll folders is similar. See below for additional info:

PyBank - Folder
* Resources - Folder
  * Contains the budget_data.csv file
* analysis - Folder
  * Contains output of main.py python script in a text file called "Financial_Analysis"
* main.py - python script

PyPoll - Folder
* Resources - Folder
  * Contains the election_data.csv file
* analysis - Folder
  * Contains output of main.py python script in a text file called "Election_Results"
* main.py - python script
