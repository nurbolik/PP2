#ex1
fruits = ["apple", "banana", "cherry"]
print(fruits[1])  # "banana"

# Output:
# banana

#ex2
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"
print(fruits)  # ["kiwi", "banana", "cherry"]

# Output:
# ["kiwi", "banana", "cherry"]

#ex3
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)  # ["apple", "banana", "cherry", "orange"]

# Output:
# ["apple", "banana", "cherry", "orange"]

#ex4
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")
print(fruits)  # ["apple", "lemon", "banana", "cherry"]

# Output:
# ["apple", "lemon", "banana", "cherry"]

#ex5
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)  # ["apple", "cherry"]

# Output:
# ["apple", "cherry"]

#ex6
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])  # "cherry"

# Output:
# cherry

#ex7
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])  # ["cherry", "orange", "kiwi"]

# Output:
# ["cherry", "orange", "kiwi"]

#ex8
fruits = ["apple", "banana", "cherry"]
print(len(fruits))  # 3

# Output:
# 3
