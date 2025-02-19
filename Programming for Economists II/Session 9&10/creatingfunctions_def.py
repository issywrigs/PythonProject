#We use the keyword def followed by a name (same rules as variable names)
#Then a list of arguments between () and then “:”
#If we do not care about arguments we use().
#The first line in the function is called the header.
#The rest is called the body, which needs to be indented.
#After the header we can add a docstring. This starts and end with “””
#To call the function, use the name followed by the arguments between ().
#To print the docstring, use help() function.

def greet():
    """
    Input: none
    This function just prints "hello"
    """
    print('Hello!')

greet()
print(help(greet))

#Most functions take some inputs and based on them, create different behavior.
def greet(name):
    """
    Input: none
    This function just prints "hello, <name> "
    """
    print('Hello,', str(name).capitalize())

greet("james")

#In this case the argument is called “name”.
#In our case, “james” is the value that will be assigned to the parameter “name” inside the function “greet”
#We must specify all arguments

#Eg. with 3 arguments

def sum_and_multiply(t1, t2, m):
    """
    :param t1: addition number1
    :param t2: addition number2
    :param m: multiplicator
    :return: prints (t1+t2)*m
    """
    print((t1+t2)*m)
sum_and_multiply(1,2,3)

#Python allows to “explicitly” bind the arguments to the value

def sum_and_multiply(t1, t2, m):
    print((t1+t2)*m)

sum_and_multiply(t2=1,m=2,t1=3)

#if we need to store the result of the previous function, we use return
#then follow it with a expression

def sum_and_multiply(t1, t2, m):
    """
    :param t1: addition number1
    :param t2: addition number2
    :param m: multiplicator
    :return: prints (t1+t2)*m
    """
    return (t1+t2)*m
result = sum_and_multiply(1,2,3)
print("(1+2)*3 - 4 = ", result-4)

#A function can call another function. We called print() inside our functions.
#we can specify default values to function parameters:
def introduce(name):
    """
    :param name: a regular string
    :return: prints the name
    """
    print("The name is:", name)

def bond(first_name="james", last_name="bond"):
    """
    Cool function
    :param first_name: first name, default "james"
    :param last_name: last name, default "bond"
    :return: returns the cool introduction
    """
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    return last_name+","+" "+first_name+" "+last_name

introduce(bond())




