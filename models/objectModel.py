from urllib import response
import requests
import json

class ObjectModelFromApi:
    def __init__(self, url):
        self.url = url
    def readAllData(self):
        try:
            clean_data = list()
            response = requests.get(self.url)
            if response.status_code == 200:
                # print('Success to fetch')
                objs = response.json()['data']['objects']
            for obj in objs:
                clean_data.append({
                    'id': obj['_id'],
                    'name': obj['name'],
                    'date': obj['date']
                })
            return clean_data # list of dictionary
        except:
            print('Failed to fetch')
            return False
    def readData(self, id):
        try:
            response = requests.get(self.url+id)
            if response.status_code == 200:
                # print('Success to fetch')
                obj = response.json()['data']
            return {
                'id': obj['_id'],
                'name': obj['name'],
                'date': obj['date']
            }
        except:
            print('Failed to fetch')
            return False
    def createData(self, payload):
        try:
            response = requests.post(self.url, json=payload)
            if response.status_code == 200:
                print(response.json()['message'])
            return True
        except:
            print('Failed to fetch')
            return False