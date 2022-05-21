from models.objectModel import ObjectModelFromApi

class ObjectControllerApi:
    def __init__(self, url):
        self.url = url
        self.model = ObjectModelFromApi(self.url)
    def getAllData(self):
        return self.model.readAllData()
    def getData(self, id):
        return self.model.readData(id)
    def addData(self, payload):
        return self.model.createData(payload)