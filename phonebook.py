from cs50 import get_string

people = {
    "Brian": "324324",
    "Map" : "435439"
}

name = get_string('Name to search: ')
if name in people:
    print(f"Number: {people[name]}")
else:
    print("Not found")