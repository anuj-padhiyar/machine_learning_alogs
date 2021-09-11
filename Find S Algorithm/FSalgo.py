import csv

with open('test2.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    table = list(csvReader)
    header = table.pop(0)
    for row in table:
        if row.pop(-1)=="yes":
            if "hypothesis" in locals():
                for i in range(len(row)):
                    if hypothesis[i] != row[i]:
                        hypothesis[i] = '?'
            else:
                hypothesis = row.copy()

    if "hypothesis" not in locals():
        print("No Data Availble")
    else:
        print(hypothesis)