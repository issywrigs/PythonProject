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

#Parsing Strings Using String Methods
#Text that you want to extract all links from
#link always starts with http:// and ends with a space
s = "http://google.com and then there could be http://yahoo.com or even a website like http://bbc.co.uk"
start = 0
while True:
    start = s.find("http://", start)
    if start == -1:
        break
    end = s.find(" ",start)
    if end == -1:
        print(s[start:])
        break
    print(s[start:end])
    start = end

#find() method finds the first occurrence of a string inside another.
# The second parameter indicates the position where to start.
# If it can not find, will return -1.