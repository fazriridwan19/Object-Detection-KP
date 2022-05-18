import datetime
import json
from scipy.fftpack import diff
import pymongo

DATA_PATH = 'F:\Object Detection Project\data'

def storeToJson(data_lists):
    json_object = json.dumps(data_lists, indent=4)

    with open("{}\data.json".format(DATA_PATH), "w") as file:
        file.write(json_object)

def loadFromJson():
    with open("{}\data.json".format(DATA_PATH), "r") as file:
        json_object = json.load(file)
    return json_object

def storeToDb(data):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["object_detection"]
    db["objects"].insert_many(data)

def createData(class_name, date):
    data = {
        "nama": class_name,
        "date": date
    }
    data_lists = loadFromJson()

    if len(data_lists) != 0:
        dateFromList = datetime.datetime.strptime(data_lists[-1]["date"], "%Y-%m-%d %H:%M:%S.%f")
        currentDate = datetime.datetime.strptime(data["date"], "%Y-%m-%d %H:%M:%S.%f")
        diff = currentDate - dateFromList

        if data["nama"] == data_lists[-1]["nama"]:
            if diff.total_seconds() > 60:
                data_lists.append(data)
                storeToJson(data_lists)
                storeToDb(data_lists)
        else:
            data_lists.append(data)
            storeToJson(data_lists)
            storeToDb(data_lists)
    else :
        data_lists.append(data)
        storeToJson(data_lists)
        storeToDb(data_lists)