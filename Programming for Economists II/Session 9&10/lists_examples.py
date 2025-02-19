#A list is a sequence of values/anything. They are MUTABLE (can change)
#A string is a sequence of only characters
#simplest way to define a list is to enclose it’s elements between [], separated by “,”

a=[]
a=[1,3,5,2,54]
a=["me", "myself", "eye"]
a = ["me", 2+3, "hey"+"you", -4.2, None]

#same rules for referencing an item inside the list that worked for strings apply to lists.
#We use the bracket operator to access elements in the list:

lst = [1, 3, 5, 7, 9]

#lists can be sliced

list = [1,2,3,4,5,6,7,8,9,10]
list[1:3] #[2, 3]
list[:4] #[1, 2, 3, 4]
list[4:] #[5, 6, 7, 8, 9, 10]
list[::3] #[1, 4, 7, 10]
list[::-1] #[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


#list operations
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
#[1, 2, 3, 4, 5, 6]

[0] * 4
#[0, 0, 0, 0]
[1, 2, 3] * 3
#[1, 2, 3, 1, 2, 3, 1, 2, 3]

a = [1,3,5]*3
print(len(a))
#9

for n in a:
...   print(n)
#lists are iterable so for function can be used

#lists have a number of methods
#To add elements to the list:
#append() adds a new element at the end of the list
#extend() takes another list and appends it to the end
#sort() arranges the elements from low to high

t = ['a', 'b', 'c']
 t.append('d')
 print(t)
#['a', 'b', 'c', 'd']
t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
t1.extend(t2)
print(t1)
#['a', 'b', 'c', 'd', 'e']
t = ['d', 'c', 'e', 'b', 'a']
t.sort()
print(t)
#['a', 'b', 'c', 'd', 'e']
t = t.sort()
print(t) #none

#To delete elements from the list:
#pop() modifies the list and returns the element that was removed. If you don't provide an index, it deletes and returns the last element.
#del operator just removes the element(s), if you do not need it anymore
#remove() deletes an element when the element is known, but not the index. It returns None. Error if the element is not present in the list

t = ['a', 'b', 'c']
x = t.pop(1)
print(t)
#['a', 'c']
print(x)
#b
t = ['a', 'b', 'c']
t.remove('b')
print(t)
#['a', 'c']
t = ['a', 'b', 'c', 'd', 'e', 'f']
del t[1:5]
print(t)
#['a', 'f']



