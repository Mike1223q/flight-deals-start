# from twilio.rest import Client
# SID = "ACfa0bf8e550a9863bf0606c1d5c3fa496"
# TOKEN = "4d9958f2822e218f0e0ce9b5ea73a7b4"
# NUMBER_FROM = "+19895752214"
# NUMBER_TO = "+15405751575"
#
#
# class NotificationManager:
#     def __init__(self, body_message):
#         client = Client(SID, TOKEN)
#         message = client.messages.create(
#             body=body_message,
#             from_=NUMBER_FROM,
#             to=NUMBER_TO
#         )

import requests
from smtplib import SMTP

my_mail = "mikesimonov414@gmail.com"
password = "tdujvhkjamcwencr"
SHEETY_ENDPOINT = "https://api.sheety.co/a7e19e0b5ba372228b1c46851c2142cc/flightDeals/users"


class NotificationManager:
    def __init__(self, body_message):

        response = requests.get(url=SHEETY_ENDPOINT)
        response.raise_for_status()
        emails = response.json()["users"]

        for email in emails:
            with SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=my_mail, password=password)
                connection.sendmail(from_addr=my_mail,
                                    to_addrs=email["email"],
                                    msg=f"Subject:Good dial!\n\n{body_message}"
                                    )

