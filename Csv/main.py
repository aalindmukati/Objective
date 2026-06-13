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

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data['temp'].to_list()

# print({data['temp'].max()})

# print(data[data.day == 'Monday'])

# print (data[data.temp == data.temp.min()])

# monday = data[data.day=='Monday']
# monday_temp = monday.temp[0]
# mtf = monday_temp * 4.25 +32
# print(mtf)

data_dict = {
    'Students':['a','b','c'],
    'marks':[96,99,98]
}
data = pd.DataFrame(data_dict)
data.to_csv("random.csv")