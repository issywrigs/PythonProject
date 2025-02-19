import random

# Create an empty list and fill it with 10 random numbers between 1 and 100
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

# Loop over the indices of the list using range()
for i in range(len(random_numbers)):
    if random_numbers[i] > 80:
        # Replace numbers greater than 80 with their negative value
        random_numbers[i] = -random_numbers[i]
    elif random_numbers[i] < 40:
        # If the number is a single digit (less than 10), sum is just the number itself
        if random_numbers[i] < 10:
            digits_sum = random_numbers[i]
        else:
            # Convert the number to string, extract digits, sum them
            digits_sum = int(str(random_numbers[i])[0]) + int(str(random_numbers[i])[1])

# Print the modified list
print(random_numbers)
