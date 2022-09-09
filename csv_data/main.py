# with open("weather_data.csv") as data_file:
#     data_list = []
#     for data in data_file:
#         data_list.append(data.strip())
#
# print(data_list)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     next(data)
#     for row in data:
#         temperatures.append(int(row[1]))
#
#     print(temperatures)

# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
#
# data_dic = data.to_dict()
# print(data_dic)
#
# temp_list = data["temp"].max()
# print(temp_list)

# print(data[data.day=="Monday"])
# print(data[data.temp == data.temp.max() ])
#
#create a data frame from scratch

# data_dict = {
#     "students": ["aravind", "vivek", "hari"],
#     "scores": [70, 72, 75]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

import pandas

data = pandas.read_csv("Squirrel_Data.csv")
# data_color = data["Primary Fur Color"].dropna()
# color_dict = {}
# for color in data_color:
#     if color in color_dict:
#         color_dict[color][0]+=1
#     else:
#         color_dict[color] = [1]
#
# print(color_dict)
# color_data = pandas.DataFrame(color_dict)
# color_data.to_csv("Squirrel_Colors")

red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
Black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
Gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])

data_dic = {
    "color" : ["Cinnamon", "Black", "Gray"],
    "count" : [red_squirrels, Black_squirrels, Gray_squirrels]
}

df = pandas.DataFrame(data_dic)
print(df)
df.to_csv("Squirrel_Colors")