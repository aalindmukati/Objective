# with open("Csv/weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

import csv


with open("Csv/weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temp = []
    for row in data:
        if row[0] != 'day':
            temp.append(row[0])
            print(row[0])