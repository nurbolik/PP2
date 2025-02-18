import math
#1
degree = float(input("Input degree: "))
radian = math.pi / 180 * degree
print("Output radian:", round(radian, 6))
#input: 16
#output: Output radian: 0.279253

#2
print("Expected output:",float(input("Height: "))*((float(input("Base, first value: "))+float(input("Base, second value: ")))/2))
#input: 10 10 8
#output: 110.0

#3
n=int(input("Input number of sides: "))
l=float(input("Input the length of a side: "))
print("The area of the polygon is:",int(n*l*l/4/math.tan(math.pi/n)))
#input: 4 25
#output: 625

#4
print("Expected Output:",float(input("Length of base: "))*float(input("Height of parallelogram: ")))
#input: 8 10
#output: 80.0