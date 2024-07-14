# importing relevant python libraries
import os
import csv

# defining variable to hold csvfile path
budget_csvpath = os.path.join('Resources','budget_data.csv')

# defining variable to hold 
with open(budget_csvpath) as budget_csvfile:
    budget_csvread = csv.reader (budget_csvfile, delimiter=',')
    print (budget_csvread)

    # storing header row
    budget_csvheader = next(budget_csvread)
    print (f"The header row for the budget_data file is {budget_csvheader}")


    row_count = 0
    Profit_Losses = [] # store all the values of the second column as list
    Changes = [] # store changes in profit and losses as a list
    Total_amount = 0

    #looping through budget_csvread file
    for row in budget_csvread:
        row_count += 1

    # populate Profit_Losses list    
        Profit_Losses.append(int(row[1]))

    # add values of the Profit_Losses list
        Total_amount += Profit_Losses[row_count-1]
    

    print (f"The total number of months in the dataset is: {row_count}")
    print (f"The net total amount of Profit/Losses is: ${Total_amount}")

    #looping through the Profit_Losses list
    for value in Profit_Losses:
        


