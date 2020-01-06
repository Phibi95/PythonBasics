# philipp = ["Philipp",24,True]

contacts = [{
    "name": "Philipp",
    "age": 24,
    "smartninjainstructor": True,
    "favorite_car_brands" : [
        "Tesla", "Porsche"
    ]
}, {
    "name": "Max",
    "age": 32,
    "smartninjainstructor": False
}, {
    "name": "Lisa",
    "age": 19,
    "smartninjainstructor": False
}]

# print(contacts[0]["name"])

for contact in contacts:
    print(contact["name"] + " ("+ str(contact["age"])+")")

print(contacts)