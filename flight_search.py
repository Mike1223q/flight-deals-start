import requests


class FlightSearch:

    def __init__(self, sheet_data):
        query_params = {
            "term": sheet_data,
            "location_types": "city",

        }
        headers = {
            "apikey": "qchgE3XDHoNtEkU3xZ3Lre4C3E7Q9hHz"
        }
        response = requests.get(url='https://api.tequila.kiwi.com/locations/query', params=query_params, headers=headers)
        response.raise_for_status()
        self.code = response.json()["locations"][0]["code"]
