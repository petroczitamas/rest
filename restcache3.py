import sys
from datetime import datetime, timedelta

import requests

URL = "https://animechan.vercel.app/api/random"


class Cache:
    cache = None

    def __init__(self):
        self.cache = {}

    def add(self, key, val):
        expire = datetime.now() + timedelta(seconds=10)
        self.cache[key] = expire, val

    def get(self, key):
        if key in self.cache:
            if datetime.now() < self.cache[key][0]:
                return self.cache[key][1]
            else:
                self.cache.pop(key)


result_cache = Cache()


def get_response_cached():
    json = result_cache.get(URL)
    if not json:
        response = requests.get(URL)
        json = response.json()
        result_cache.add(URL, json)

    return json


if __name__ == "__main__":
    while True:
        prompt = input("Would you like an anime quote? Y/N ")
        if prompt.lower() == "y" or prompt.lower() == "n":
            if prompt.lower() == "y":
                print(get_response_cached())
            else:
                sys.exit()
        else:
            print("Invalid response, try again.")
            pass
