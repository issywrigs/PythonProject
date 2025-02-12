#lets create a virtual diary
with open("diary.txt", "w") as fp:
    while True:
        text = input("How do you feel today?")
        if text == "q":
            break
        fp.write(f"{text}/n") # this is the same as below line
        # fp.write(text + "/n")
        