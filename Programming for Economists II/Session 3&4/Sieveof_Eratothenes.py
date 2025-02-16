# creating a list of the first n numbers
n = 50  # n can be whatever number
x = list(range(2, n + 1))

for i in x:
    j = 2
    while (i * j <= x[-1]):
        if (i * j in x):
            x.remove(i * j)
        j += 1

print("The list of prime numbers is:", x)
