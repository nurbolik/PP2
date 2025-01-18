#ex1
x = "Hello World"
print(len(x))
#output : 11

#ex2
txt = "Hello World"
x = txt[0]
print(x)
#output : H

#ex3
txt = "Hello World"
x = txt[2:5]
print(x)
#output : llo

#ex4
txt = " Hello World "
x = txt.strip()
print(x)
#output : Hello World

#ex5
txt = "Hello World"
txt = txt.upper()
print(txt)
#output : HELLO WORLD

#ex6
txt = "Hello World"
txt = txt.lower()
print(txt)
#output : hello world

#ex7
txt = "Hello World"
txt = txt.replace("H","J")
print(txt)
#output : Jello World

#ex8
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
#output : My name is John, and I am 36