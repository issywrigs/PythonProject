#Opening a file tells the operating system we want to use that file
#so the operating system locates the file,makes sure it exists and gets it ready for us.
#we use the built in function open().
#The first parameter is the filename (path included)
#second parameter is the “mode”.
#The modes are: r – read (default), w – write, x – exclusive creation, a – append, b – binary, t – text (default), + – update (read + write)
#result of the open() is assigned to a variable, called file descriptor
#to avoid errors, must use try/ except


fp=open("text.txt","r") # r 1 by default, so not really needed
print(fp.read()) # prints the entire content of the file
fp.close() # good practice to close the file

# same exact thing with context manager
with open("text.txt","r") as fp:
    print(fp.read())

# let's read from the same file, line by line
print("Read the file line by line")
with open("text.txt","r") as fp:
    for line in fp:# we iterate over the file, line by line (prints lines in between each sentence)
        print(line)

        # or
print("Read the file line by line")
with open("text.txt","r") as fp:
    for line in fp:# we iterate over the file, line by line (prints lines in between each sentence)
        print(line, end= "") #add a print not to add a new line

        print(line.rstrip())

print("Read the file line by line")
line_number=1
with open("text.txt", "r") as fp:
    for line in fp:
        print(f"{line_number}: {line}", end ="" )
        line_number +=1




