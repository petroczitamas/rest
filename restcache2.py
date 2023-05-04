import sys

import requests

choice = input("Do you want all todos? Y/N ")

if choice.lower() == "y" or choice.lower() == "n":
    if choice.lower() == "y":
        url_end = "todos"
    else:
        todo_number = input("Enter todo number: ")
        url_end = f"todos/{todo_number}"
else:
    print("Invalid response, exiting.")
    sys.exit()

URL = f"https://jsonplaceholder.typicode.com/{url_end}"


def get_response():
    response = requests.get(URL)

    json: dict = response.json()

    print(json)


if __name__ == "__main__":
    get_response()
