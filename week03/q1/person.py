import json

import requests


def part_one():
    with open('person.json', "r") as read_file:
        json_objects = json.load(read_file)
        for obj in json_objects:
            print(f"{obj['age']}")


def part_two():
    response = requests.get('https://jsonplaceholder.typicode.com/users')

    json_objects = json.loads(response.text)
    for obj in json_objects:
        print(json.dumps(obj['address'], indent=4))


part_two()
