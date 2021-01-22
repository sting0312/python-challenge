import os
import csv
sum_total = 0
row_count = 0
csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter= ",")
        print(csvreader)
        #skip header for csv file
        csv_header = next(csvreader)
        #print Header
        print(f"CSV Header: {csv_header}")
        #print test csv
        
        for row in csvreader:
            print(row)
            sum_total += float(row[1])
            row_count = row_count + 1


        #row_count = len(list(csvreader))
print(f"Financial Analysis")
print(f"-----------------------------")
print(f"Total Months:", row_count)
print(f"Total:" , sum_total)

