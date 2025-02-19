#How many times does the letter e appear in the short text?
def number_times(filename, letter):
    fd = open(filename)
    times = 0
    for line in fd:
        times = times + line.count(letter)
    fd.close()
    return times


print("The letter e turns up", number_times("short.txt", "e"), "times")

#How many times do the 2 most common letters appear i the text file?
def most_common(filename):
    fd = open(filename)
    letters = "abcdefghijklmnopqrstuvwxyz"
    dic = {}
    for line in fd:
        for letter in line:
            if letter in letters:
                if letter in dic:
                    dic[letter] += 1
                else:
                    dic[letter] = 1

    list_values = list(dic.values())

    list_values.sort(reverse=True)
    fd.close()
    print("the two most common letters appear", list_values[0] + list_values[1], "times")


most_common("short.txt")