from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import  NotificationManager


data_manager = DataManager()

for dates in data_manager.sheet_data:
    city = dates["city"]
    flight_search = FlightSearch(city)
    dates["iataCode"] = flight_search.code


# data_manager.update_iata()
for dict in data_manager.sheet_data:
    code = dict["iataCode"]
    flight_data = FlightData(code)
    fly_date_from = flight_data.data['route'][0]['local_arrival'].replace("T", " ").split()[0]
    fly_date_to = flight_data.data['route'][-1]['local_arrival'].replace("T", " ").split()[0]

    fly_city_from = flight_data.data['cityFrom']
    fly_code_from = flight_data.data['flyFrom']

    fly_city_to = flight_data.data['cityTo']
    fly_code_to = flight_data.data['cityCodeTo']

    fly_link = flight_data.data['deep_link']

    # print(f"{dict['city']}: £{flight_data.min_price}")
    body_message = f"Only GBP{flight_data.min_price} to fly from {fly_city_from}" \
                   f"-{fly_code_from} to {fly_city_to}-{fly_code_to}, " \
                   f"from {fly_date_from} to {fly_date_to}.\n{fly_link}"
    try:
        if dict["lowestPrice"] >= flight_data.min_price:
            NotificationManager(body_message)
            print("1")
        else:
            print("2")
    except:

        print("3")


