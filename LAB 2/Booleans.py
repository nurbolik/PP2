#ex1
print("ex1")
print(10 > 9)  # True
print(10 == 9)  # False
print(10 < 9)  # False

# Output:
# ex1
# True
# False
# False

#ex2
print("ex2")
a = 10
b = 9

if b > a:  # False
    print("b is greater than a")
else:
    print("b is not greater than a")

# Output:
# ex2
# b is not greater than a

#ex3
print(bool("Hello"))  # True
print(bool(15))  # True

# Output:
# True
# True

#ex4
print("ex4")
a = "Hello"
b = 15
print(bool(a))  # True
print(bool(b))  # True

# Output:
# ex4
# True
# True

#ex5
print("ex5")
print(bool("abc"))  # True
print(bool(123))  # True
print(bool(["Mercedes", "Volvo", "BMW"]))  # True

# Output:
# ex5
# True
# True
# True

#ex6
print("ex6")
print(bool(False))  # False
print(bool(None))  # False
print(bool(0))  # False
print(bool(""))  # False
print(bool(()))  # False
print(bool([]))  # False
print(bool({}))  # False

# Output:
# ex6
# False
# False
# False
# False
# False
# False
# False

#ex7
print("ex7")
class myclass():
    def __len__(self):
        return 0


myobj = myclass()
print(bool(myobj))  # False

# Output:
# ex7
# False

#ex8
print("ex8")
def myFunction():
    return True


print(myFunction())  # True

# Output:
# ex8
# True

#ex9
print("ex9")
def myFunction():
    return True


if myFunction():  # True
    print("YES!")
else:
    print("NO!")

# Output:
# ex9
# YES!

#ex10
print("ex10")
x = 200
print(isinstance(x, int))  # True

# Output:
# ex10
# True
