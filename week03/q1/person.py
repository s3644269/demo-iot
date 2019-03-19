import json

import requests


def part_one():
    with open('person.json', "r") as read_file:
        data = json.load(read_file)
        for obj in data:
            print(f"{obj['age']}")

def part_two():
    # id = input('Which id: ')
    response = requests.get(f'https://jsonplaceholder.typicode.com/users/')
    data = json.loads(response.text)

    for obj in data:
        print(json.dumps(obj, indent=4))


part_two()
