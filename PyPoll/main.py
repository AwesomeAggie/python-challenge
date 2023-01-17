import pandas as pd
import csv

csv_file=pd.read_csv("Resources/election_data.csv")
#setting variables
Total=len(csv_file)
Charles=0
Diana=0
Raymon=0
Other=0
#first section text
print("Election Results")
print("----------------------------")
print("Total Votes: ",
        Total)
print("----------------------------")
#counter for the votes
with open("Resources/election_data.csv","r") as reader:
    csv_reader=csv.reader(reader)
    next(csv_reader)
    for row in csv_reader:
        if row [2]=="Charles Casper Stockham":
            Charles+=1
        elif row [2]=="Diana DeGette":
            Diana+=1
        elif row[2]=="Raymon Anthony Doane":
            Raymon+=1
        else:
            Other+=1
#New Variables for percentage
Cper=(Charles/Total)*100
Dper=(Diana/Total)*100
Rper=(Raymon/Total)*100
#second section print out
print("Charles Casper Stockham: ",str(round(Cper,3)),"% ","(",Charles,")")     
print("Diana DeGette: ",str(round(Dper,3)),"% ","(",Diana,")") 
print("Raymon Anthony Doane: ",str(round(Rper,3)),"% ","(",Raymon,")") 
print("----------------------------")
#third section print out with winner
if Cper > Dper and Cper > Rper:
    print("Winner: Charles Casper Stockham")
elif Dper > Cper and Dper > Rper:
    print("Winner: Diana DeGette")
elif Rper > Cper and Rper > Dper:
    print("Winner: Raymon Anthony Doane")
print("----------------------------")
#print to text file
f=open("analysis/analysis.txt", 'w')
f.write("Election Results")
f.write('\n')
f.write("----------------------------")
f.write('\n')
f.write("Total Votes: ")
f.write(str(Total))
f.write('\n')
f.write("----------------------------")
f.write('\n')
f.write("Charles Casper Stockham: ")
f.write(str(round(Cper,3)))
f.write("% ")
f.write("(")
f.write(str(Charles))
f.write(")")
f.write('\n')
f.write("Diana DeGette: ")
f.write(str(round(Dper,3)))
f.write("% ")
f.write("(")
f.write(str(Diana))
f.write(")")
f.write('\n')
f.write("Raymon Anthony Doane: ")
f.write(str(round(Rper,3)))
f.write("% ")
f.write("(")
f.write(str(Raymon))
f.write(")")
f.write('\n')
f.write("----------------------------")
f.write('\n')
if Cper > Dper and Cper > Rper:
    f.write("Winner: Charles Casper Stockham")
elif Dper > Cper and Dper > Rper:
    f.write("Winner: Diana DeGette")
elif Rper > Cper and Rper > Dper:
    f.write("Winner: Raymon Anthony Doane")
f.write('\n')
f.write("----------------------------")