#Suppose we want to write data to a file as well.
#In this case we need to open the file for writing.
#The modes are “w” – write and “a” – append.
#“w” – will start with an empty file no matter what, “a” will append to the end if the file already exists.

#lets create a virtual diary
with open("diary.txt", "w") as fp:
    while True:
        text = input("How do you feel today?")
        if text == "q":
            break
        fp.write(f"{text}/n") # this is the same as below line
        # fp.write(text + "/n")

#Once the file has been opened, we use the write() method.
#Unlike print(), write() will not append a newline character at the end

fp = open("text.txt", "a")
print(fp)
line = input("Give me some text, don't be shy: ")
fp.write(line)
fp.write("\n")
fp.close()

#Running this program repeatedly will keep appending to the file