# write comment like this
print("Hello Issy")
print("As you can see, each print will start from a new line")
# to make sure all code continues on 1 line we can do the following
print("we need to use the end argument, ", end="") #end is just the line of text added to the end of the print
print("so we continue on the same line", end="(end can be whatever we want). ")

print(2+4)
print("the value of 2+5 is ", 2+5)
print("Python, is 2 greater than 4? the answer is: ", 2 > 4)
print("we can use print as a calculator: ", (2 + 3*2)**2)  # same as (2 + 6) to the power of 2 = 8 x 8 = 64

print("dog", "cat", "mouse", "elephant", "moose")
#  sep argument can be used to seperate the items with something- below is done with !!
print("dog", "cat", "mouse", "elephant", "moose", sep="!!   ",
      end="! just one exclamation for moose\n") #\n means that the next print will be on a new line

