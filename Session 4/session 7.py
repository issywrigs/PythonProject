# sum the first 10 numbers
sum= 0
for num in range(1,101): #11 is excluded, so it goes from 1 to 10
    sum= sum + num
print(sum)

# print multiplication table
for i in range(1,11):
    for j in range(1,11):
        print(f"{i} x {j}= {i*j}")

#with while
sum=0
num=0
while num< 100:
    num=num + 1
    sum+= num
print(sum)

