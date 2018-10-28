import os
import csv
csvpath = os.path.join("..", "Resources", "data.csv")
file_to_output = os.path.join("analysis", "budget_analysis.txt")
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    

#The total number of months included in the dataset
total_month=0
    
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for month in csvreader:
        total_month = total_month + 1
     


#The total net amount of "Profit/Losses" over the entire period
total_net=0

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
       total_net = total_net + int(row[1])


#The average change in "Profit/Losses" between months over the entire period

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    first_row = next(csvreader)
    prev_net = int(first_row[1])
    net_change_list = []
    month_change= []
    greatest_increase = ["",0]
    greatest_decrease = ["", 9999999999]

    for row in csvreader:
      net_change = int(row[1]) - prev_net
      prev_net = int(row[1])
      net_change_list = net_change_list + [net_change]
      month_change = month_change + [row[0]]
      net_monthly_avg = sum(net_change_list) / len(net_change_list)
      net_monthly_avg=int(net_monthly_avg)

      if net_change > greatest_increase[1]:
          greatest_increase[0] = row[0]
          greatest_increase[1] = net_change

      if net_change < greatest_decrease[1]:
          greatest_decrease[0] = row[0]
          greatest_decrease[1] = net_change
      


output = (
    f"\nFiancial Analysis\n"

    f"----------------------------\n"

    f"Total Months: {total_month}\n"
    
    f"Total: ${total_net}\n"

    f"Average Change: ${net_monthly_avg:.2f}\n"
    
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"

    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

print(output)

