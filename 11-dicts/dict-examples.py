names = ["Philipp","Lisa","Max","Moritz"]


# while True:
#     new_name = input("insert new Name to List: ")
#
#     names.append(new_name)
#     #names.insert(0,new_name)
#
#     for name in names:
#         print(name)

print(names[0])

contacts = [
    {
        "name" : "Tom",
        "age": 45
    },
    {
        "name" : "Philipp",
        "age" : 24
    }
]

for contact in contacts:
    print(contact["name"])

mixed_list = [22, "elon", True, "SmartNinja", 3.14]
print(mixed_list)
# mixed_list.sort() !!!
# print(mixed_list)

some_list = [34.449 ,1, 34.45, 12, 17, 87]
print(some_list)
some_list.sort()
print(some_list)
print(some_list[:3])


print(names)
names.sort()
print(names)