#sometimes we iterate through things like a list of numbers, letters in a string, lines in a file
#DEFINITE LOOP as there is a finite number of steps and then it ends

result = 0
for i in range(0,10):
    result += i
print("The sum of the first 9 numbers is", result)

result = 0
text = "1234567890"
for i in text:
    result += int(i)
print("The sum of the first 9 numbers is", result)

#The range type represents a sequence of numbers that is used for looping a specific number of times inside a for loop.
#range(start, stop[, step])

#known number of iterations
#Can end via break
#Can start from the beginning via continue
#Uses a counter
#Always can be re-written with a while statement
