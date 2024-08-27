
#
# with open("weather_data.csv") as f:
#      data = f.readlines()
# print(data)

# import csv
#
# with open("weather_data.csv") as  data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] == 'temp':
#             pass
#         else:
#             temperature.append(int(row[1]))
#     for i in temperature:
#         print(i)


import pandas
data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
# print(data['temp'].mean())
# print(data["temp"].max())
#
# #Get Data in Columns
# print(data["condition"])
#print(data.condition)

# # Get Data in Row
# print(data[data.day == "Monday"])
#
print(data[data.temp == data.temp.max()])
####################################################################################
# Create file with "Pandas"
data_dict = {
    "students":["Amy", "James", "Angela"],
    "socre": [76,56,65]
}

data = pandas.DataFrame(data_dict)
print(data)
#Create CSV file from dictionary
data.to_csv("new_data.csv")
############################################################
