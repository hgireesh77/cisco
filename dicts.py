dict1 = {
    "name": "Gireesh Hariharasubramony",
    "Org": "HCLTECH",
    "Pincode": 695019,
    "Vehicles": ["Tata Tigor", "Merida Crossway 20"]
}
#print the data type
print(type(dict1))
#print the dictionary items
print(dict1)
#print the value for the key "Vehicles"
print(dict1["Vehicles"])
#Replaces the whole present dictionary items with the new key/value pair 
dict1 = {"New key": "New value"}
#print the dictionary items
print(dict1)
#Replaces the whole present dictionary items with the new key/value pair
dict1 = {
    "name": "Gireesh Hariharasubramony",
    "Org": "HCLTECH",
    "Pincode": 695018,
    "Vehicles": ["Tata Tigor", "Merida Crossway 20"]
}
#print the dictionary items
print(dict1)
#Adds the new key and value to the whole dictionary
dict1.update({"New Key": "New Value"})
#print the dictionary items
print(dict1)
#update the dictionary item "Pincode"
dict1["Pincode"] = 695019
#print the dictionary items
print(dict1)
#Pop will delete the item specified as the key
dict1.pop("Pincode")
#print the dictionary items
print(dict1)

dict1 = {
    "name": "Gireesh Hariharasubramony",
    "Org": "HCLTECH",
    1: 695018,
    "Vehicles": ["Tata Tigor", "Merida Crossway 20"]
}
#print the dictionary items
print(dict1)
#Popitem removes or deletes the last key/value pair
dict1.popitem()
#print the dictionary items
print(dict1)