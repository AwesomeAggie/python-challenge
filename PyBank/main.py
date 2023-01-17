import pandas as pd
import csv

csv_file=pd.read_csv("Resources/budget_data.csv")
#First section print
print("Financial Analysis")
print("----------------------------")
print("Total Months: ",
        len(csv_file))
print("Total: $",csv_file["Profit/Losses"].sum())
#Finding the values for second section
csv_file["new_column"]=csv_file["Profit/Losses"].shift(1)
csv_file["difference"]=csv_file["Profit/Losses"]-csv_file["new_column"]
average= csv_file["difference"].mean()
average=str(round(average,2))
max=csv_file["difference"].max()
max_date=csv_file.sort_values("Profit/Losses").tail(1).Date
min=csv_file["difference"].min()
min_date=csv_file.sort_values("Profit/Losses").head(1).Date
#Second section print
print("Average Change: $",average)
print("Greatest Increase in Profits: ",max_date.to_string(index=False), int(max))
print("Greates Decrease in Profits: ",min_date.to_string(index=False), int(min))
#Write the text file
f=open("analysis/analysis.txt", 'w')
f.write("Financial Analysis")
f.write('\n')
f.write("----------------------------")
f.write('\n')
f.write("Total Months: ")
f.write(str(len(csv_file)))
f.write('\n')
f.write("Total: $")
f.write(str(csv_file["Profit/Losses"].sum()))
f.write('\n')
f.write("Average Change: $")
f.write(average)
f.write('\n')
f.write("Greatest Increase in Profits: ")
f.write(max_date.to_string(index=False))
f.write("  ($")
f.write(str(int(max)))
f.write(")")
f.write('\n')
f.write("Greatest Decrease in Profits: ")
f.write(min_date.to_string(index=False))
f.write("  ($")
f.write(str(int(min)))
f.write(")")