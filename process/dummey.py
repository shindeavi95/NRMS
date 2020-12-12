import requests

url = "https://www.fast2sms.com/dev/bulk"
message = "This is Avinash , this message is for only test, please do not replay"
querystring = {
               "authorization":"P3imuaqY6dlDKEVUx9Cvz2QLHMpSonjwAX5kFI1s7WftrGNeg8dKjhDoIkW78xlsJaReZQimXn35qvg1",
               "sender_id":"FSTSMS",
               "message": message,
               "language":"english",
               "route":"p",
               "numbers":"9403552332"
               }

headers = {
    'cache-control': "no-cache"
}

response = requests.request("GET", url, headers=headers, params=querystring)
json_data = 
print(response.text)