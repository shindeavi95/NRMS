import requests
import json
# from django.http import HttpResponse
# from django.shortcuts import render
# from django.core.mail import send_mail
# from RMS.settings import EMAIL_HOST_USER


def sendTextMessage(message, contact):
    url = "https://www.fast2sms.com/dev/bulk"

    querystring = {
        "authorization": "3puK7H9SYkR1SAfFURbO6cYd86tVK5AH9IjLITYl5jTR4kgBbA9ItepMCrg7",
        "sender_id": "FSTSMS",
        "message": message,
        "language": "english",
        "route": "p",
        "numbers": contact,
    }

    headers = {
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    json_data = response.text
    d1 = json.loads(json_data)
    return d1['return']


#
# def sendMail(request):
#     # send_mail('subject', 'message','EMAIL_HOST_USER',['recipient_List'])
#     send_mail('Welcome To RMS',
#               'This is test mail',
#               'EMAIL_HOST_USER',
#               ['avinashshinde999.as@gmail.com'])
#
#     return HttpResponse("Mail is send")
