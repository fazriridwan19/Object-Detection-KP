import datetime
from controllers.objectController import ObjectControllerApi

def createData(class_name, date):
    data = {
        "name": class_name,
        "date": date
    }
    obj = ObjectControllerApi('http://localhost:3000/api/v1/objects/')
    data_list = obj.getAllData()
    # data_list = loadFromJson()

    if len(data_list) != 0:
        dateFromList = datetime.datetime.strptime(data_list[-1]["date"], "%Y-%m-%d %H:%M:%S.%f")
        currentDate = datetime.datetime.strptime(data["date"], "%Y-%m-%d %H:%M:%S.%f")
        diff = currentDate - dateFromList

        if data["name"] == data_list[-1]["name"]:
            if diff.total_seconds() > 60:
                obj.addData(data)
                # data_list.append(data)
                # storeToJson(data_list)
                # storeToDb(data_list)
        else:
            obj.addData(data)
            # data_list.append(data)
            # storeToJson(data_list)
            # storeToDb(data_list)
    else :
        obj.addData(data)
        # data_list.append(data)
        # storeToJson(data_list)
        # storeToDb(data_list)