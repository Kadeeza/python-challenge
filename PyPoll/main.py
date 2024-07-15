# importing relevant python libraries
import os
import csv

# defining variable to hold csvfile path
election_csvpath = os.path.join("..","PyPoll","Resources","election_data.csv")

# opening csv file
with open(election_csvpath) as election_csvfile:
    election_csvread = csv.reader (election_csvfile, delimiter=',')

    # storing header row
    election_csvheader = next(election_csvread)
   
    # initializing variables
    row_count = 0
    Charles_count = 0
    Diana_count = 0
    Raymon_count= 0

    #looping through budget_csvread file
    for row in election_csvread:
        #print (row[2])
        row_count += 1
        if row [2] == "Charles Casper Stockham":
            Charles_count += 1
        elif row[2] == "Diana DeGette":
            Diana_count += 1
        else:
            Raymon_count += 1
           
    # calculating percentage of votes
    Total_Votes = row_count
    Percent_Charles = round((Charles_count/Total_Votes)*100, 3)
    Percent_Diana = round((Diana_count/Total_Votes)*100, 3)
    Percent_Raymon = round ((Raymon_count/Total_Votes)*100, 3)
    
    # Determining winner
    Max_percent = max([Percent_Charles, Percent_Diana, Percent_Raymon])
    print(Max_percent)

    if Max_percent == Percent_Charles:
        Winner = "Charles Casper Stockham"
    elif Max_percent == Percent_Diana:
        Winner = "Diana DeGette"
    else:
        Winner = "Raymon Anthony Doane"
    
    # printing results
    print (f" Election Results \n ------------------------ \n Total Votes: {Total_Votes} \n ------------------------ \n Charles Casper Stockham: {Percent_Charles}% ({Charles_count}) \n Diana DeGette: {Percent_Diana}% ({Diana_count}) \n Raymon Anthony Doane: {Percent_Raymon}% ({Raymon_count}) \n ------------------------ \n Winner: {Winner}")

# writing results to .txt file
output_path = os.path.join("..","PyPoll","analysis","Election_Results.txt")
with open(output_path,"w") as election_txtfile:
    election_txtfile.write (f" Election Results \n ------------------------ \n Total Votes: {Total_Votes} \n ------------------------ \n Charles Casper Stockham: {Percent_Charles}% ({Charles_count}) \n Diana DeGette: {Percent_Diana}% ({Diana_count}) \n Raymon Anthony Doane: {Percent_Raymon}% ({Raymon_count}) \n ------------------------ \n Winner: {Winner}")
