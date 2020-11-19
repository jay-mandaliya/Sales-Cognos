import csv
from datetime import datetime
from pathlib import Path

columns = []
data = []

with open(Path("../data/sales_data.csv"), "r") as dataFile:
	csvReader = csv.reader(dataFile)

	columns = next(csvReader)

	for row in csvReader:
		data.append(row)

for row in data:
	dateObject = ""

	if("-" in row[5]):
		dateObject = datetime.strptime(row[5], "%m-%d-%Y %H:%M")
	else:
		dateObject = datetime.strptime(row[5], "%m/%d/%Y %H:%M")

	row[5] = dateObject.strftime("%Y") + "-" + dateObject.strftime("%m") + "-" + dateObject.strftime("%d")


with open(Path("../data/clean_data.csv"), "w", newline='', encoding='utf-8') as dataFile:
	csvWriter = csv.writer(dataFile)

	csvWriter.writerow(columns)
	csvWriter.writerows(data)