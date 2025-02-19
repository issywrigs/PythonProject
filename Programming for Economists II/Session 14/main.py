from China import cook as China_cook
from Senegal import cook as Senegal_cook
import sys
import pandas
print("hello world")

from China import greet

def greet():
    print("hello from Segoland")

China_cook()
greet() #no need to use china as we imported it directly

print(China_cook())
print(Senegal_cook())


