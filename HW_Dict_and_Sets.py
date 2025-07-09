person = {
    "name": "Ivan",
    "age": 30,
    "city": "Sofia"
}

print("name      :", person["name"])
print("age       :", person["age"])
print("city      :", person["city"])

person["job"] = "Developer"
print(person)

person["age"] = 31
print(person)


del person["job"]
print(person)


print("age" in person)


extra_info = {"job": "Developer", "salary": 50000}
merged_person = {**person, **extra_info}
print(merged_person)


for key, value in person.items():
    print(f"{key}: {value}")