# with open("Csv/weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv


# with open("Csv/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temp = []
#     for row in data:
#         if row[1] != 'temp':
#             temp.append(row[1])
            
# print(f'So the temperatures are {temp}')

import pandas as pd 
data = pd.read_csv("Csv/weather_data.csv")
# print(type(data))
# # print(data['day'])

data_dict = data.to_dict()
print(data_dict)