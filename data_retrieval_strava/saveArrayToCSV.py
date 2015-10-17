# save array into CSV file
import csv

def saveArrayToCSV(info_array, file_name):
    with open(file_name, "a") as f:
        writer = csv.writer(f)
        writer.writerows(info_array)
