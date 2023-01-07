import requests
from pprint import pprint

SHEETY_ENDPOINT = "https://api.sheety.co/a7e19e0b5ba372228b1c46851c2142cc/flightDeals/prices"


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        # get_sheety_response = requests.get(SHEETY_ENDPOINT)
        # self.sheet_data = get_sheety_response.json()["prices"]
        # for dict in self.sheet_data:
        #     if dict["iataCode"] == "":
        #         dict["iataCode"] = "TESTING"
        # # pprint(sheet_data)
        # for new in self.sheet_data:
        #     row = {"price": new}
        #     put_sheety_response = requests.put(url=f"{SHEETY_ENDPOINT}/{str(new['id'])}", json=row, )
        #     put_sheety_response.raise_for_status()
        # print(self.sheet_data)
        self.sheet_data = [{'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 54, 'id': 2}, {'city': 'Berlin', 'iataCode': 'BER', 'lowestPrice': 42, 'id': 3}, {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 485, 'id': 4}, {'city': 'Sydney', 'iataCode': 'SYD', 'lowestPrice': 551, 'id': 5}, {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 95, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 414, 'id': 7}, {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 240, 'id': 8}, {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 260, 'id': 9}, {'city': 'Cape Town', 'iataCode': 'CPT', 'lowestPrice': 378, 'id': 10}, {'city': 'Bali', 'iataCode': 'DPS', 'id': 11}]


    def update_iata(self):
        for new in self.sheet_data:
            row = {"price": new}
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{str(new['id'])}", json=row, )
            response.raise_for_status()
