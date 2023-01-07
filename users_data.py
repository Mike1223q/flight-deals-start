import requests


USERS_ENPOINT = "https://api.sheety.co/a7e19e0b5ba372228b1c46851c2142cc/flightDeals/users"

print("Welcome to Mike's Flight Club!\nWe find the best flight deals and email you.")
# first_name = input("What's your first name?\n")
first_name = "Mike"
# last_name = input("What's your last name?\n")
last_name = "Simonov"
# email = input("What's your email?\n")
email = "mikesimonov313@gmail.com"
# repeat_email = input("Type your email again.\n")
repeat_email = "mikesimonov313@gmail.com"
if email == repeat_email:
    parameters = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
        }
    }
    response = requests.post(url=USERS_ENPOINT, json=parameters)
    response.raise_for_status()





else:
    print("Wrong email, please try again.")






