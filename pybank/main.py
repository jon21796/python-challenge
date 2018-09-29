import csv
import os
raw_data=('03-Python_homework_PyBank_Resources_budget_data copy.csv')
new_data=('NEW03-Python_homework_PyBank_Resources_budget_data copy.txt')

total_months = 0
prev_revenue = 0
month_of_change = []
revenue_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_revenue = 0

with open(raw_data) as data:
    reader = csv.DictReader(data)
    for row in reader:
        
        total_months = total_months + 1
        total_revenue = total_revenue + int(row["Profit/Losses"])

        revenue_change = int(row["Profit/Losses"]) - prev_revenue
        prev_revenue = int(row["Profit/Losses"])
        revenue_change_list = revenue_change_list + [revenue_change]
        month_of_change = month_of_change + [row["Date"]]

        if (revenue_change > greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = revenue_change

        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = revenue_change

revenue_avg = sum(revenue_change_list) / len(revenue_change_list) 
        
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Revenue: ${total_revenue}\n"
    f"Average Revenue Change: ${revenue_avg}\n"
    f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

with open(new_data, "w") as txt_file:
    txt_file.write(output)