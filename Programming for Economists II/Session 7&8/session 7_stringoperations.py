s1= "hello"
s2= "world"
print(s1 + " " +s2) # quotation marks ensure there is a space between the 2 words
# addition always works between 2 strings, but multiplication can only be between a string and a positive integer
# note, 1 slash does division and 2 slashes only produce integers

#strings can be compared. “==“ returns True if the strings are identical
#<, > performs alphabetical comparison
#note: uppercase letters are smaller than lowercase

hi = "banana"
hi == "banana" #True
hi == "Banana" #False
hi < "Banana" #False
hi > "bana" #True


#in operator takes two strings and returns True if the first is a substring of the second
"ba" in hi #True
"baN" in hi #False
