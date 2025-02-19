#decisions can be performed using the if function. Everything with a truth value can be used in a conditional

if_stmt ::=  "if" expression ":" suite
             ( "elif" expression ":" suite )*
             ["else" ":" suite]

#selects exactly one of the suites by evaluating the expressions one by one until one is found to be true
#then that suite is executed (and no other part of the if statement is executed or evaluated).
#If all expressions are false, the suite of the else clause, if present, is executed

if number % 2 == 0:
    print(number, "is an even number")
    print(“Nothing would be printed if it were odd”)

if number % 2 == 0:
    print(number, "is an even number")
else
    print(number, "is an odd number")

#In this case we have the True branch and the False branch

#Sometimes there are more than two possibilities and we need more than two branches = CHAINED CONDITIONAL
if a > b:
    print(a, ">", b)
elif a < b:
    print(a, "<", b)
else:
    print(a, "=", b)

if a == b:
    print(a, "=", b)
else:
    if a < b:
        print(a, "<", b)
    else:
        print(a, ">", b)

#no limit to elif branches


