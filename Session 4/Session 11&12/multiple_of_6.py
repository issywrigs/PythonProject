#Write a function that forces the user to enter a multiple of 6 number. Use try, except to catch invalid inputs. Return that number
def get_multiple_of_six():
    """
    Returns a multiple of 6 that was entered by the user
    :return: int a number
    """
    while True:
        try:
            n= input("Please give me a multiple of 6:")
            n= int(n) #convert to int
            #how to check if it is a multiple of 6?
            if n % 6 == 0:
                return n
            #another way to check:
            elif n / 6 == n // 6:
                return n
            else:
                print("That is not a multiple of 6")
        except ValueError:
            print("You have not entered a number")

print(get_multiple_of_six())




