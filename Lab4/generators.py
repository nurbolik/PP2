#1
def sqgen(n):
    for i in range(1,n+1):
        yield i*i
n=int(input("N: "))
print(*sqgen(n))
#input: 5
#output: 1 4 9 16 25

#2
def evgen(n):
    for i in range(0,n,2):
        yield i
n=int(input("n: "))
print(*evgen(n),sep=", ")
#input: 10
#output: 0, 2, 4, 6, 8

#3
def divgen(n):
    for i in range(0,n):
        if i%3==0 or i%4==0:
            yield i
n=int(input("n: "))
print(*divgen(n))
#input: 20
#output: 0 3 4 6 8 9 12 15 16 18

#4
def squares(a,b):
    for i in range(a,b+1):
        yield i*i
a=int(input(("a: ")))
b=int(input(("b: ")))
for i in squares(a,b):
    print(i,end=" ")
print()
#input: 3 7
#output: 9 16 25 36 49

#5
def revgen(n):
    for i in range(n,-1,-1):
        yield i
n=int(input("n: "))
print(*revgen(n))
#input: 5
#output: 5 4 3 2 1 0