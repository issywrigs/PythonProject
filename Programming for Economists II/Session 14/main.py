import random
import china, austria
from austria import cook as austria_cook
from china import cook as china_cook
from latam.argentina import cook as argentina_cook
from latam.brazil import cook as brazil_cook
from latam.mexico.yucantan import cook as yucatan_cook

def cook():
    print("we are making paella")

print("a random number is:", random.randint(1, 10))
china_cook()
china.greet()
austria_cook()
austria.greet()
cook()
argentina_cook()
brazil_cook()
yucatan_cook()