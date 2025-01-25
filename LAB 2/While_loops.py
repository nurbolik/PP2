#ex1
i = 1
while i < 6:
    print(i)  # 1, 2, 3, 4, 5
    i += 1

# Output:
# 1
# 2
# 3
# 4
# 5

#ex2
i = 1
while i < 6:
    if i == 3:
        break
    i += 1

# Output:
# (This will print 1 and 2, then break when i == 3)

#ex3
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)  # 1, 2, 4, 5, 6

# Output:
# 1
# 2
# 4
# 5
# 6

#ex4
i = 1
while i < 6:
    print(i)  # 1, 2, 3, 4, 5
    i += 1
else:
    print("i is no longer less than 6")  # "i is no longer less than 6"

# Output:
# 1
# 2
# 3
# 4
# 5
# i is no longer less than 6
