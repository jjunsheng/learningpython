#dictionary to store information that comes as key value
#customer has attributes, can be stored. each key has to be unique

customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
customer["name"] = "Jack Smith"
print(customer.get("birthdate", "Jan 1 1980"))

print(customer["name"])
print(customer["age"])
print(customer["is_verified"])

#what if
print(customer["birthdate"])
print(customer["Name"])