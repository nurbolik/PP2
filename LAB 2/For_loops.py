#ex1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)  # "apple", "banana", "cherry"

# Output:
# apple
# banana
# cherry

#ex2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)  # "apple", "cherry" (skips "banana")

# Output:
# apple
# cherry

#ex3
for x in range(6):
    print(x)  # 0, 1, 2, 3, 4, 5

# Output:
# 0
# 1
# 2
# 3
# 4
# 5

#ex4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)  # "apple" (stops at "banana")

# Output:
# apple
