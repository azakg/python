import pandas

"""
In this code we are getting information from CSV file, like Color of the Suqirrels (Grey, Cinnamon and Black)
count amount of each of them
"""
# This is reading file
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240826.csv")



#This is get amoutn of the Cinnamon Squirrels
cinnamon_squirrel_count = len(data[data["Highlight Fur Color"] == "Cinnamon"])
grey_squirrel_count = len(data[data["Highlight Fur Color"] == "Gray"])
black_squirrel_count = len(data[data["Highlight Fur Color"] == "Black"])


data_dic = {
    "Fur Color": ["Grey", "Cinnamon", "Black"],
    "Count": [cinnamon_squirrel_count, grey_squirrel_count, black_squirrel_count]
            }

# Convert form python Dictionary into pandas DataFrame
df = pandas.DataFrame(data_dic)
df.to_csv("squirrel_count.csv")