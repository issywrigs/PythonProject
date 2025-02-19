#the most versatile way of parametrizing a string
#syntax is like the one used by .format()
print(f"The sum of 1 + 2 is {1+2}")

name = "Eric"
age = 74
f"Hello, {name}. You are {age}." # 'Hello, Eric. You are 74.'

#Inside the {} you can use any expression, call functions or methods
def to_lowercase(input):
    return input.lower()
name = "Issy Wrigley"
print(f"{to_lowercase(name)} thinks she is funny.") #issy wrigley thinks she is funny.


