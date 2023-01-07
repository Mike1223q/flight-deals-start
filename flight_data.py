import requests
from pprint import pprint
from datetime import datetime, timedelta

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"


class FlightData:
    def __init__(self, code):

        now = datetime.now().today()
        delta_tomorrow = (now + timedelta(days=+1)).date().strftime("%d/%m/%Y")
        delta_6_months = (now + timedelta(weeks=26)).date().strftime("%d/%m/%Y")
        returns_from = (now + timedelta(days=+8)).date().strftime("%d/%m/%Y")
        returns_to = (now + timedelta(days=+29)).date().strftime("%d/%m/%Y")
        headers = {
            "apikey": "qchgE3XDHoNtEkU3xZ3Lre4C3E7Q9hHz"
        }

        parameters = {
            "fly_to": code,
            "fly_from": "LON",
            "date_from": delta_tomorrow,
            "date_to": delta_6_months,
            # "limit": "2",
            "curr": "GBP",
            "return_from": returns_from,
            "return_to": returns_to,

        }
        response = requests.get(url=TEQUILA_ENDPOINT, params=parameters, headers=headers)
        response.raise_for_status()

        self.min_price = 0
        self.all_data = response.json()
        self.data = None
        for result in self.all_data["data"]:
            price = (result["price"])
            if self.min_price < price:
                self.min_price = price
                self.data = result
