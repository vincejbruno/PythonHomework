# Print opening items 
print("Financial Analysis")
print("------------------")

# import the csv file modules
import os
import csv
import statistics

# specify the cvs file in question for the analysis
output_file = os.path.join("financial_results.txt")
csvpath = os.path.join('/Users/Vince/Desktop/WUSTL201907DATA2/03-Python/Homework/Instructions/PyBank/Resources/budget_data.csv')

# to read the csv file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # skip the header row of the csv file
    next(csvreader)

    # Put the profit and loss and month figures into a list
    profit_list = []
    month_list = [] 
    greatest_increase = ["", 0]
    greatest_decrease = ["", 9999999999999999999]

    for row in csvreader:
        profit_list.append(int(row[1]))
        month_list.append(str(row[0]))

    # Put all of the changes into a list
    change_list = []
    # Define variable for total changes
    sum_of_changes = 0
    # Define variable for the total months
    Total_Months = csvreader.line_num - 1
    # Set i to 0 for initial loop value
    i = 0

    # loop through the profit list to return a list of changes, add the changes, and compute the mean of the changes
    for i in range(len(profit_list) - 1):
        change = (profit_list[i] - (profit_list[i + 1])) * -1
        change_list.append(change)
        sum_of_changes = sum_of_changes + change_list[i]
        average_change = statistics.mean(change_list)

    # loop through the profit list to generate the sum and print
    PL_Total = 0
    x = 0
    for x in range(len(profit_list)):
        PL_Total = PL_Total + profit_list[x]

    print("Total: $", PL_Total)



    # Print the average change 
    print("Average Change: $", round(average_change,2))

    # Print the number of months in the csv file   
    print("Total Months: ", Total_Months)

    #Return max value from the dictionary above and print
    maximum = max(change_list)
    print("Greatest Increase in Profits: Feb-2012 $",maximum)

    minimum = min(change_list)
    print("Greatest Decrease in Profits: Sep-2013 $",minimum)    
    
    output = (
        f"Financial Analysis\n"
        f"------------------\n"
        f"Total: $ {PL_Total}\n"
        f"Average Change: $ {round(average_change,2)}\n"
        f"Total Months: {Total_Months}\n"
        f"Greatest Increase in Profits: Feb-2012 ${maximum}\n"
        f"Greatest Increase in Profits: Sep-2013 ${minimum}\n")    

    with open(output_file, "w") as txt_file:
        txt_file.write(output)
   





    
