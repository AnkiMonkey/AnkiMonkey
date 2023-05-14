#Merging csv files

import csv

# Create a new CSV file to write the merged data to
with open("merged.csv", "w", newline="", encoding="utf-8") as merged_file:
    writer = csv.writer(merged_file)

    # Loop through each CSV file and write its data to the merged file
    for i in range(1, 7):
        filename = f"{i}.csv"
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                writer.writerow(row)


