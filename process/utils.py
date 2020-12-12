import requests
import json


def sendTextMessage(message,contactno):


        url = "https://www.fast2sms.com/dev/bulk"

        querystring = {
                       "authorization":"P3imuaqY6dlDKEVUx9Cvz2QLHMpSonjwAX5kFI1s7WftrGNeg8dKjhDoIkW78xlsJaReZQimXn35qvg1",
                       "sender_id":"FSTSMS",
                       "message": message,
                       "language":"english",
                       "route":"p",
                       "numbers": contactno,
                       }

        headers = {
            'cache-control': "no-cache"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        json_data = response.text
        d1 = json.load(json_data)

        return d1['return']
