#ex1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
    print("Yes, apple is a fruit!")  # Yes, apple is a fruit!

# Output:
# Yes, apple is a fruit!

#ex2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)  # {"apple", "banana", "cherry", "orange"}

# Output:
# {"apple", "banana", "cherry", "orange"}

#ex3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print(fruits)  # {"apple", "banana", "cherry", "orange", "mango", "grapes"}

# Output:
# {"apple", "banana", "cherry", "orange", "mango", "grapes"}

#ex4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)  # {"apple", "cherry"}

# Output:
# {"apple", "cherry"}

#ex5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)  # {"apple", "cherry"}

# Output:
# {"apple", "cherry"}
