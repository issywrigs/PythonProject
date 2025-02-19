#executing the same action more than once is called an iteration or a loop.
#main statements that allow iteration in Python are while and for

#initialize a “counter” variable before execution
#Test the counter variable in the while
#Operate (increment/decrement) the “counter” inside the loop

n = 1
result = 0

while n < 10:
    result += n
    n += 1
print("The sum of the first 9 numbers is", result)

#sometimes we don't know before how many iterations we need
#loop ,must be broken when certain condition met
#BREAK and CONTINUE are used to stop the current iteration and start from the beginning again

while True:
    num = input("Give me a number (type quit to exit)")
    num2 = input("Give me another number(type quit to exit)")
    if num == "quit" or num2 == "quit":
        break
    num = int(num)
    num2 = int(num2)
    if num2 == 0:
        print("Can not divide by zero")
        continue
    print("The division result of", num, "and", num2, "is", num/num2)
