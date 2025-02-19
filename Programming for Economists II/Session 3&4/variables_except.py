#In Python we assign things with the equal (=) sign: speed = 120.4 The left hand side of the expression is a name we call the variable. The right hand side is the value we associate with it, in our case a float number
#Names can be arbitrarily long, contain both letters and numbers, but can not start with a number, contain the underscore (_) character
#33 Keywords that cant be used as var names = and del from None True as elif global nonlocal try assert else  if not while break except import or with class False in pass yield continue finally is raise def for lambda return

#input function: program stops and waits for the user to type something. Value returned is a string
#if string is input in words, ca n convert to number via int() or float()

#exceptions are when code is syntactically correct but you have mis-written some parts Eg.spelling, incorrect numbers

#try and except can prevent a crash caused by an exception if an invalid number is entered

try:
    num = input("Give me a number")
    num = int(num)
    num2 = input("Give me another number")
    num2 = int(num2)
    result = num / num2
    print("The division result is", result)

except ValueError:
    print("Please give me a proper number")
except ZeroDivisionError:
    print("The second number can not be zero")
except:
    print("Some other exception I did not see coming")
else:
    print("The division result is", result)
