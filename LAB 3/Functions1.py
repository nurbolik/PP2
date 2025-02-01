#ex1
from array import array
def ounce(grams):
    print("ounces =", grams*28.3495231)
ounce(float(input("grams: ")))
#input : 3
#output : ounces = 85.0485693

#ex2
def celcius(fahrenheit):
    print("celcius =",(5/9)*(fahrenheit-32))
celcius(int(input("fahrenheit: ")))
#input : 4
#output : celcius = -15.555555555555557

#ex3
def solve(numheads, numlegs):
    print("rabbits =", int((numlegs - numheads - numheads) / 2))
    print("chickens =", int(numheads - (numlegs - numheads - numheads) / 2))
numheads = int(input("numheads : "))
numlegs = int(input("numlegs : "))
solve(numheads, numlegs)
#input : 35
#input : 94
#output : rabbits = 12
#output : chickens = 23

#ex4
def filter_prime(n):
    count = 0
    for i in range(1, n + 1):
            if n % i == 0:
                count += 1
    return count == 2
l = [x for x in map(int,input("list: ").split()) if filter_prime(x)]
print("primes:", l)
#input: list: 1 5 17 15 18
#output: primes: [5, 17]

#ex5
from itertools import permutations
def permutate(s):
    p = permutations(s)
    for i in p:
        print(''.join(i))
s = input()
permutate(s)
#input : abc
"""
output : abc
         acb
         bac
         bca
         cab
         cba 
"""

#ex6
def reverse(s):
    for i in range(len(s)):
        print(s[len(s)-i-1])
reverse(list(map(str, input("string: ").split())))
#input: string : Hello World
"""
output : World
         Hello
"""

#ex7
def has_33(n):
    s=""
    for i in range(len(n)):
        s+=str(n[i])
        if(s.count("33")>=1):
            return "True"
    return "False"
print(has_33(list(map(int,input("numbers: ").split()))))
#input : 1 3 3 1
#output: True

#ex8
def spy_game(n):
    s=""
    for i in range(len(n)):
        s+=str(n[i])
        if(s.count("007")>=1):
            return "True"
    return "False"
print(spy_game(list(map(int,input("numbers: ").split()))))
#input : 1 2 4 0 0 7 5
#output : True

#ex9
import math
def volume(radius):
    return 4*math.pi*pow(radius,3)/3
print(volume(float(input("radius: "))))
#input : 4
#output : 268.082573106329

#ex10
def unique(l):
    l.sort()
    for i in range(len(l)-1,0,-1):
        if(l[i]==l[i-1]):
            l.remove(l[i])
    print(l)
unique(list(input("list: ").split()))
#input : 1 1 2 2 3 3
#output : ['1', '2', '3']


#ex11
def pal(s):
    return s==s[::-1]
print(pal(input("phrase: ")))
#input: ziz
#output: True

#ex12
def histogram(l):
    for i in range(len(l)):
        print("*"*l[i])
histogram(list(map(int,input("list: ").split())))
#input : 4 2 4
""" 
output : ****
         **
         ****
"""
#ex13
import random
def guess(s):
    r=random.randint(1,20)
    print(f"\nWell, {s}, I am thinking of a number between 1 and 20.")
    b=False
    i=0
    while(b==False):
        i+=1
        n=int(input("Take a guess\n"))
        if(r==n):
            print(f"\nGood job, {s}! You guessed my number in {i} guesses!")
            b=True
        elif(r>n):
            print("\nYour guess is too low.")
        else:
            print("\nYour guess is too high.")
guess(input("Hello! What is your name? \n"))
"""
Hello! What is your name? 
Nurbol

Well, Nurbol, I am thinking of a number between 1 and 20.
Take a guess
4

Your guess is too low.
Take a guess
10

Your guess is too low.
Take a guess
14

Your guess is too low.
Take a guess
18

Your guess is too high.
Take a guess
15

Good job, Nurbol! You guessed my number in 5 guesses!

"""
