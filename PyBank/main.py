import os
import csv
sum_total = 0
row_count = 0
average_change=0
average_change_list = []
average_change_month = []
previous_month = 0
greatest_increase = 0
greatest_decrease = 0
csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter= ",")
        print(csvreader)
        #skip header for csv file
        csv_header = next(csvreader)
        #print Header
        #print(f"CSV Header: {csv_header}")
        #print test csv
        
        for row in csvreader:
            #print(row)
            sum_total += float(row[1])
            row_count = row_count + 1
            monthly_change = int(row[1]) - previous_month
            previous_month = int(row[1])
            average_change_list.append(monthly_change)
            average_change_month.append(row[0])

            average_change = sum(average_change_list) / len(average_change_list)
            #print(monthly_change)
            greatest_increase = max(average_change_list)
            greatest_index= average_change_list.index(greatest_increase)
            greatest_month= average_change_month[greatest_index]

            greatest_decrease = min(average_change_list)
            worst_index= average_change_list.index(greatest_decrease)
            worst_month= average_change_month[worst_index]

            




        #row_count = len(list(csvreader))      
print(f"Financial Analysis")
print(f"-----------------------------")
print(f"Total Months: ", row_count)
print(f"Total: " , sum_total)
print(f"Average Change: ", average_change)
print(f"Greatest Increase in Profits: ", greatest_month, ":  ",greatest_increase)
print(f"Greatest Increase in Profits: ", worst_month, ":  ",greatest_decrease)


output_path = os.path.join("Analysis", "PyBank_Analysis.txt")

with open(output_path, "w") as text_file:

    print("Financial Analysis", file = text_file)
    print("-----------------", file = text_file)
    print("Total Months: ", row_count, file = text_file)
    print("Total: " , sum_total, file = text_file)
    print("Average Change: ", average_change, file = text_file)
    print("Greatest Increase in Profits: ", greatest_month, ":  ",greatest_increase, file = text_file)
    print("Greatest Increase in Profits: ", worst_month, ":  ",greatest_decrease, file = text_file)