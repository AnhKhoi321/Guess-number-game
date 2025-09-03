# dictionary = a collection of {key: value} pairs 
#              ordered and changeable. No duplicates

capitals = {"USA": "Washinton D.C",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}
# print(dir(capitals))
# print(help(capitals))

# print(capitals.get("Japan"))

# if capitals.get("Japan"):
#     print("That capital exists")
# else:
#     print("That capital doesn't exist")

# capitals.update({"Germany": "Berlin"}) # thay doi thu ben trong thu vien
# capitals.update({"USA": "Detroit"})
# capitals.pop("China") # bo thu dc goi 
# capitals.clear() # bo toan bo thu vien


# keys = capitals.keys() # lay lai toan bo noi dung chinh

# for key in capitals.keys():
#     print(key)

# values = capitals.values() # lay lai cac gia tri co trong thu vien
# for value in capitals.values():
#     print(value)

items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")
