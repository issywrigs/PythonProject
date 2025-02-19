#A string is a collection of any characters contained in double or single quotations
#It is non-scalar, we can get pieces out of it
#We use square brackets, and the indentation starts with zero
#indexing returns another string. It must be an integer less than the string length.
#You can assign a string to a variable
s1="banana"
s2='banana'
print(s1,s2)
s1= 'And jon said: "How are you?". The person replied:"I\'m smart"'
print(s1)
s1= "I can print \"and another \""
print (s1)

# indexing, starts from 0
s = "0123456789"
print(s[1],s[7],s[9])
print(s[-1], s[-4])
print(f"the length is: {len(s)}")
#len() will return the length of a string.
#This is a general function that can be used with other non-scalar objects.


hi = "Hello"
bye = "Bye"
hi+bye #HelloBye'
print(hi + " " + bye) #'Hello Bye'
#The “+” operator is overloaded for strings and produces the concatenation

#* operator is overloaded for strings and it allows to multiply a string with a number.
#The result is the string repeated “number” of times
3 * "abc" # abcabcabc
bye = hi * 4 # 'HelloHelloHelloHello‘

#String is “iterable” so for can be used to get each element
for letter in hi:
    print(letter)


