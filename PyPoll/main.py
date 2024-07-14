# importing relevant python libraries
import os
import csv

# defining variable to hold csvfile path
election_csvpath = os.path.join('Resources','election_data.csv')

# opeming csv file
with open(election_csvpath) as election_csvfile:
    election_csvread = csv.reader (election_csvfile, delimiter=',')

    # storing header row
    election_csvheader = next(election_csvread)
    print (f"The header row for the budget_data file is {election_csvheader}")


    row_count = 0

    #looping through budget_csvread file
    for row in election_csvread:
        row_count += 1
    Total_Votes = row_count
    print (row_count)