'''
"""
ex1 - המרת גיל לחודשים
"""
x = float(input("Hi, Enter your age please: "))
age = 12*x
print(f"Your age in months is: {age} months")


"""
ex2 - 
"""
x = float(input("Hi, Enter your age in months please: "))
age = x/12
print(f"Your age in years is: {age} years")

"""
ex3
"""

x = float(input("Enter a number pleas: "))
if x % 7 == 0:
    print("Boom")
else:
    print("The number is not divisible by 7 ")

"""
ex4
"""
x = int(input("enter a number pleas: "))
if x % 7 == 0:
    print("Boom")
elif '7' in str(x):
    print("Boom")
else:
    print("a not 7's number")

"""ex5"""
x = int(input("Enter 3 Number pleas: \n1: "))
y = int(input("2: "))
z = int(input("3: "))
print(max(x, y, z))
'''

"""
ex6
"""
print("We want to calculate the sum of an invoice series")
a1 = int(input("enter a first number of the series:\na1:= "))
d = int(input("enter a The series difference of the series:\nd:= "))
n = int(input("Write down the number of members of the series:\nn:= "))

sumOfSeries = (2*a1 + (n-1)*d)*(n/2)
print(f"the sum of series is {sumOfSeries}")

