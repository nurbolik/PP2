#ex1
a = 50
b = 10
if a > b:
    print("Hello World")  # "Hello World"

# Output:
# Hello World

#ex2
a = 50
b = 10
if a != b:
    print("Hello World")  # "Hello World"

# Output:
# Hello World

#ex3
a = 50
b = 10
if a == b:
    print("Yes")
else:
    print("No")  # "No"

# Output:
# No

#ex4
a = 50
b = 10
if a == b:
    print("1")
elif a > b:
    print("2")  # "2"
else:
    print("3")

# Output:
# 2

#ex5
a = 6
b = 8
c = 5
if a == b and c == d:
    print("Hello")  # This will not print since d is not defined

# Output:
# (Nothing is printed)

#ex6
a = 6
b = 8
c = 5
d = 6
if a == b or c == d:
    print("Hello")  # "Hello"

# Output:
# Hello

#ex7
if 5 > 2:
    print("YES")  # "YES"

# Output:
# YES

#ex8
a = 2
b = 5
print("YES") if a == b else print("NO")  # "NO"

# Output:
# NO

#ex9
a = 2
b = 50
c = 2
if a == c or b == c:
    print("YES")  # "YES"

# Output:
# YES
