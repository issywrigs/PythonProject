d= {} # empty dictionary
eng_to_spa = {"one": "uno", "two": "dos", "three": "tres"}
print(eng_to_spa)
eng_to_spa["I"] = "yo"
eng_to_spa["am"] = "soy"
eng_to_spa["spanish"] = "español"
print(eng_to_spa)
sentence = "I am spanish"
words= sentence.split()
for word in words:
    print(eng_to_spa[word])
eng_to_spa.update({"yes": "si", "no": "no"}) #update dictionary with new dict
print(eng_to_spa)

#print(eng_to_spa.popitem()) #not very helpful as you don't know which is the last item
print(eng_to_spa.pop("two")) #much better to pop a value by specifying the key

if "tree" in eng_to_spa:
    print(eng_to_spa["tree"])
else:
    print("I don't know that word")

print(eng_to_spa.get("tree","unknown word"))

for key in eng_to_spa:
    print(f"{eng_to_spa[key]} means {key}")

for key, value in eng_to_spa.items():
    print(f"{value} means {key}")