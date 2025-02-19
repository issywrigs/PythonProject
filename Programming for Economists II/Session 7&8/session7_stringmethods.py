#Strings are an example of Python objects
#An object contains both data (the actual string itself) and methods
#Python's function dir() lists the methods available for an object
#The help() function can be used to get a short description of a method

s = "hello world my name is John"
s.capitalize() #Hello....
s.center(40) # shifts along
s.count(" ") #5, counts spaces
s.replace(" ","!!") # replaces all spaces with 2 exclamation marks
s.split() # makes each word seperate in its own quotations

s= "hello"
print(dir(s)) #gives a list of methods
print(help(s.capitalize))
print(s.capitalize)
print("HELLO".casefold())
print("hello".center(50))
print("hello".center(50, "*"))


print("banananananananana". count("ana"))


