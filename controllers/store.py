import datetime
import time
import os
import json

from scipy.fftpack import diff
DATA_PATH = 'F:\Object Detection Project\data'

def storeToJson(data_lists):
    json_object = json.dumps(data_lists, indent=4)

    with open("{}\data.json".format(DATA_PATH), "w") as file:
        file.write(json_object)

def loadFromJson():
    with open("{}\data.json".format(DATA_PATH), "r") as file:
        json_object = json.load(file)
    return json_object

def createData(class_name, date):
    data = {
        "nama": class_name,
        "date": date
    }
    data_lists = loadFromJson()
    dateFromList = datetime.datetime.strptime(data_lists[-1]["date"], "%Y-%m-%d %H:%M:%S.%f")
    currentDate = datetime.datetime.strptime(data["date"], "%Y-%m-%d %H:%M:%S.%f")
    diff = currentDate - dateFromList

    if data["nama"] == data_lists[-1]["nama"]:
        if diff.total_seconds() > 30:
            data_lists.append(data)
            storeToJson(data_lists)
    else:
        data_lists.append(data)
        storeToJson(data_lists)
    
# createData("car", str(datetime.datetime.now()))
# # datetime(year, month, day, hour, minute, second)
# a = datetime.datetime(2022, 4, 11, 10, 0, 0)
# b = datetime.datetime(2022, 4, 11, 10, 0, 40)

# # returns a timedelta object
# c = b-a
# print('Difference: ', c.total_seconds())

# minutes = c.total_seconds() / 60
# print('Total difference in minutes: ', minutes)

# # returns the difference of the time of the day
# minutes = c.seconds / 60
# print('Difference in minutes: ', minutes)
