punctuation = ".,%!?"

def find_words(filename):
    """
    prints the 3 letter words starting with b
    :param filename:
    :return:
    """
    with open(filename, 'r') as f:
        for line in f:
            #sanitise line
            for p in punctuation:
                line=line.replace(p," ")
            # need to break down the line into words
            words=line.split() # by default splits by space
            # check each word
            for word in words:
                if len(word) == 3 and word.upper()[0] == "B": #this ensures that capital letters are included
                    print(word)
find_words("input.exp")
