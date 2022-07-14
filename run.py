import requests as req
import time

def spam(reqId):

    response = req.get('https://api.mobilelegends.com/mlweb/sendMail?roleId='+ str(reqId) + '&language=en')

    return response.json()

    
if __name__ == '__main__':

    reqId = int(input('\n? ID : '))
    reqHowMuch = int(input('? How much : '))
    print(' ')

    while True:

        if spam(reqId)['status'] == 'success':
            print('[ ' + time.strftime("%H:%M:%S") + ' ] Success sent !')
            time.sleep(60)

        elif spam(reqId)['code'] == '-20023':
            print('[ ' + time.strftime("%H:%M:%S") + ' ] Error sent ! Invalid ID')
            break

        else:
            continue
