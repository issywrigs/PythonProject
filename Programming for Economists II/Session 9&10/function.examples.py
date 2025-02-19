#functions help us understand entire programs
#they provide Modularity (break it into smaller problems), Abstraction, Readability, Reusability of code
#function = reusable piece of code

#1st define the function: give it a name, define a set of parameters and then provide the sequence of operations for that function
#function won't run unless called
#functions can have a doc string, telling the user what the function does
#Once defined, you “call” the function as many times as you want for the function to produce its effects

def greet():
    """
    Simple function that just prints hello
    :return: None
    """
    print("Hello!")

def greet2(name):
    """
    Simple function that greets a person
    :param name: The name of a person
    :return: None
    """
    print(f"Hello,{name}")

greet2("Jane")
greet2("Mary")

def special_op(a=1,b=1):
    """
    :param b: second number
    :return: value, 10a + b
    """
    return 10*a + b
print(special_op(10,2))
print(special_op(2,10))
result= special_op(8,9)
print(f"the special op for 8 and 9 is {result}")
print(special_op(b=8,a=9))
print(special_op())
print(special_op(a=9))

def bond_greet(name):
    print(f"The name is: {name}")

def bondise_name(first_name= "James", last_name= "Bond"):
    return f"{last_name}, {first_name} {last_name}"

print(bondise_name("John", "Doe"))
bond_greet(bondise_name(first_name="John",last_name="Doe"))




