name = input("What is your name?")
print("hello", name)

try:
    age=input("How old are you?")

except ValueError:
    print("you are trying to trick me")

except ZeroDivisionError:
    print("you can't divide by 0")

except:
    print("something unexpected happened")

else:
    print("you were probably born in", 2024 - int(age))

a=30
b=20
if a > b:
    print(a, "is greater than", b)
elif a==b:
    print(a, "is equal to", b)
else:
    print (a,"is less than", b)

from random import choice
drinks={"gin", "vodka", "whiskey", "rum"}
name= input("I am the virtual bartender. What is your name?")
try:
    age= input("What is your age?")
    age= int(age)
except:
    country= input("What is your country?")

