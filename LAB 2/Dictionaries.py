#ex1
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))  # "Mustang"

# Output:
# Mustang

#ex2
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020
print(car)  # {"brand": "Ford", "model": "Mustang", "year": 2020}

# Output:
# {"brand": "Ford", "model": "Mustang", "year": 2020}

#ex3
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car["color"] = "red"
print(car)  # {"brand": "Ford", "model": "Mustang", "year": 1964, "color": "red"}

# Output:
# {"brand": "Ford", "model": "Mustang", "year": 1964, "color": "red"}

#ex4
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
print(car)  # {"brand": "Ford", "year": 1964}

# Output:
# {"brand": "Ford", "year": 1964}

#ex5
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
print(car)  # {}

# Output:
# {}
