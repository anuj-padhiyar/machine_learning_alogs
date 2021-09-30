import csv

with open('test1.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    table = list(csvReader)
    header = table.pop(0)

hypothesis = []
for row in table:
    if row.pop(-1)=="yes":
        if len(hypothesis) != 0:
            for i in range(len(row)):
                if hypothesis[i] != row[i]:
                    hypothesis[i] = '?'
        else:
            hypothesis = row.copy()

if len(hypothesis) == 0:
    print("No Data Availble")
else:
    print("Hypothesis Is ",hypothesis)
