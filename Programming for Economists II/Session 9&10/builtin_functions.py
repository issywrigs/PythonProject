#useful built in functions:
#min(), max(), len()
#Conversion functions: int(), float(), str()

#random values
import random

for i in range(10):
    x = random.random()
    print(x)

random.randint(5, 10)

ppl = ["Jon", "Ana", "Maria", "Jim", "Florence", "George", "James"]
random.choice(ppl)
