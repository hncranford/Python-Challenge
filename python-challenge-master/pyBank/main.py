#what we need
#total number of months included in the dataset
#net total amount of "Profit/Losses" over the entire period
#average of the changes in "Profit/Losses" over the entire period
#greatest increase in profits (date and amount) over the entire period
#greatest decrease in losses (date and amount) over the entire period
import os
import csv

csvpath=os.path.join("Resources","budget_data.csv")

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    month = []
    revenue = []
    revenue_change = []
    monthly_change = []


    for row in csvreader:
        month.append(row[0])
        revenue.append(row[1])

    revenueInt = map(int,revenue)
    total_revenue = (sum(revenueInt))


    i = 0
    for i in range(len(revenue) - 1):
        profit_loss = int(revenue[i+1]) - int(revenue[i])
        revenue_change.append(profit_loss)
    Total = sum(revenue_change)
   
    monthly_change = Total / len(revenue_change)
    

    profit_increase = max(revenue_change)
    h = revenue_change.index(profit_increase)
    month_increase = month[h+1]
    
    profit_decrease = min(revenue_change)
    l = revenue_change.index(profit_decrease)
    month_decrease = month[l+1]
        
    
f = open("Analysis/Analysis.txt","w")
f.write ("Financial Analysis")
f.write ("---------------------------")
f.write("Total Months:" +str(len(month)))
f.write("Total: $"+str(total_revenue))
f.write("Average Change: $"+str(monthly_change))
f.write(f"Greatest Increase in Profits: {month_increase} ${profit_increase}")
f.write(f"Greatest Decrease in Profits: {month_decrease} ${profit_decrease}")

print("Financial Analysis")
print("---------------------------")
print("Total Months:" +str(len(month)))
print("Total: $"+str(total_revenue))
print("Average Change: $"+str(monthly_change))
print(f"Greatest Increase in Profits: {month_increase} ${profit_increase}")
print(f"Greatest Decrease in Profits: {month_decrease} ${profit_decrease}")



