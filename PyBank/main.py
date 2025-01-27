# importing relevant python libraries
import os
import csv

# defining variable to hold csvfile path
budget_csvpath = os.path.join("..","PyBank","Resources","budget_data.csv")

# defining variable to hold 
with open(budget_csvpath) as budget_csvfile:
    budget_csvread = csv.reader (budget_csvfile, delimiter=',')

    # storing header row
    budget_csvheader = next(budget_csvread)
    

    row_count = 0
    Profit_Losses = [] # store all the values of the second column as list
    Changes = [] # store changes in profit and losses as a list
    Total_amount = 0 # sum of Profit_Losses column

    #looping through budget_csvread file
    for row in budget_csvread:
        row_count += 1

    # populate Profit_Losses list    
        Profit_Losses.append(int(row[1]))

    # add values of the Profit_Losses list
        Total_amount += Profit_Losses[row_count-1]
    
    Total_count = row_count
    
    # looping through the Profit_Losses list
    for i in range(len(Profit_Losses)-1):
        Changes.append (Profit_Losses[i+1]-Profit_Losses[i])
    

    #Find average change
    Average_Change = round(sum(Changes)/len(Changes), 2)    
    
    #Find Max increase and decrease in profits
    Max_change = max(Changes)
    Min_change = min(Changes)

    #Print analysis to the terminal
    print (f" Financial Analysis \n ------------------------------- \n Total Months: {Total_count} \n Total: ${Total_amount} \n Average Change: ${Average_Change} \n Greatest Increase in Profits: (${Max_change}) \n Greatest Decrease in Profits: (${Min_change})")

# Write results to .txt file
output_path = os.path.join("..","PyBank","analysis","Financial_Analysis.txt")
with open(output_path,"w") as Finance_txtfile:
     Finance_txtfile.write (f" Financial Analysis \n ------------------------------- \n Total Months: {Total_count} \n Total: ${Total_amount} \n Average Change: ${Average_Change} \n Greatest Increase in Profits: (${Max_change}) \n Greatest Decrease in Profits: (${Min_change})")




