people = [
    {"name": "Michael", "house": "Duplex"},
    {"name": "Mercy", "house": "Terrace"},
    {"name": "Marvellous", "house": "Ravenclaw"}
]

def f(person):
    return person["name"]

people.sort(key=f)

print(people)