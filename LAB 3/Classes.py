#ex1
class Cla:
    def __init__(self):
        self.s=""
    def getString(self):
        self.s=input("string: ")
    def printString(self):
        print(self.s.upper())
x=Cla()
x.getString()
x.printString()
#input : hello
#output : HELLO

#ex2
class Shape:
    def area(self):
        self.a=0
        print("area:",self.a)
class Square(Shape):
    def __init__(self):
        self.length=int(input("length: "))
    def area(self):
        self.a=self.length*self.length
        print("area:",self.a)
x=Square()
x.area()
#input : 5
#output : 25

#ex3
class Rectangle(Shape):
    def __init__(self):
        self.length=int(input("length: "))
        self.width=int(input("width: "))
    def area(self):
        self.a=self.length*self.width
        print("area: ",self.a)
x=Rectangle()
x.area()

#input : 10 5
#output : 50

#ex4
import math
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(f"point: {self.x}, {self.y}")
    def move(self, nx, ny):
        self.x = nx
        self.y = ny
        print(f"new point: {self.x} , {self.y}")
    def dist(self):
        x2, y2 = int(input("2nd point x: ")), int(input("2nd point y: "))
        distance = math.sqrt((x2 - self.x) ** 2 + (y2 - self.y) ** 2)
        print("distance:",distance)

x1, x2 = int(input("x: ")), int(input("y: "))
result = Point(x1, x2)
result.show()
nx, ny = int(input("new x: ")), int(input("new y: "))
result.move(nx, ny)
result.dist()
"""
input:
x: 3
y: 4
new x: 6
new y: 8
2nd point x: 10
2nd point y: 12

output:
point: 3, 4
new point: 6, 8
distance: 5.656854249492381
"""
#ex5
class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def deposit(self,d):
        self.d = d
        self.balance += self.d
        print("balance:", self.balance)
    def withdraw(self,w):
        self.w = w
        p = True
        self.balance -= self.w
        if self.balance < 0:
            p = False
            self.balance += self.w
            print("no money withdraw")
        print("balance:",self.balance)
owner = input("owner: ")
balance = int(input("balance: "))
x = Account(owner, balance)
x.deposit(int(input("deposit: ")))
x.withdraw(int(input("withdraw: ")))
x.deposit(int(input("deposit: ")))
x.withdraw(int(input("withdraw: ")))
x.deposit(int(input("deposit: ")))
x.withdraw(int(input("withdraw: ")))

"""
input:
owner: John
balance: 1000
deposit: 500
withdraw: 200
deposit: 300
withdraw: 1500
deposit: 1000
withdraw: 500

output: 
balance: 1500
balance: 1300
balance: 1600
no money to withdraw
balance: 1600
balance: 2600
balance: 2100
"""
#ex6
nums = list(map(int,input().split()))
def prime(x):
    if x==1:
        return False
    else:
        for i in range(2, x):
            if x%i==0:
                return False
        return True
print(list(filter(prime,nums)))
#input : 2 3 4 5 6 7 8 9 10 11
#output : [2, 3, 5, 7, 11]