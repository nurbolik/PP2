print("Ex1")
#ex1
l = list(map(int,input().split()))
print(eval('*'.join(map(str,l))))
#input: 10 5 2
#output: 100

print("Ex2")
#ex2
s = input()
l = list(filter(lambda x: x.isupper(),s))
u = list(filter(lambda x: x.islower(),s))
print(f"lowercase: {len(l)}, uppercase: {len(u)}")
#input: Hello World
#output: lowercase: 2, uppercase: 8

print("Ex3")
#ex3
a = input()

is_palindrome = all(a[i] == a[-i - 1] for i in range(len(a)))

print(is_palindrome)
#input: 1001
#output: True

print("Ex4")
#ex4
import time
a=float(input("Sample input:\n"))
t=float(input())
time.sleep(t/1000)
print(f'Sample output:\nSquare root of {a} after {t} milliseconds is {a**0.5}')
#input: 16 1000
#output: Square root of 16.0 after 1000 milliseconds is 4.0

print("Ex5")
#ex5
user_input = input()
mytuple = tuple(map(lambda x: x.strip().capitalize() == "True", user_input.split(' ')))
x = all(mytuple)
print(x)
#input: True True True
#ouput: True
