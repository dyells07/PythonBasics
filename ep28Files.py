import csv

with open('data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        revenue = int(row['Revenue'])
        print(f"Revenue for {row['Month']} {row['Year']}: {revenue}")
