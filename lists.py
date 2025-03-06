Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# A list of integers
number_list=[1,2,3,4,5,6,7,8]
# Acessing Elements
print(number_list[0])
1
print(number_list[3])
4
#negative indexing
print(number_list[-1])
8
print(number_list[-3])
6
#Adding elements
number_list.append('9')
print(number_list)
[1, 2, 3, 4, 5, 6, 7, 8, '9']
number_list.append(10)
print(number_list)
[1, 2, 3, 4, 5, 6, 7, 8, '9', 10]
#Insert: Adds an item at a specific position.
number_list.insert(0, 0)
print(number_list)
[0, 1, 2, 3, 4, 5, 6, 7, 8, '9', 10]
# Removing Elements: Removes the first instance of the specified value.
number_list.remove(9)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    number_list.remove(9)
ValueError: list.remove(x): x not in list
number_list.remove('9')
print(number_list)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 10]
#Pop: Removes an element by index (default is the last element) and returns it.
last_number = number_list.pop()
print(last_fruit)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print(last_fruit)
NameError: name 'last_fruit' is not defined
last_number = number_list.pop()
print(last_number)
8
#Clear: Removes all elements from the list.
number_list.clear()
print(fruit_list)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print(fruit_list)
NameError: name 'fruit_list' is not defined
number_list.clear()
print(number_list)
[]
>>> #Slicing Lists: access a range of elements in a list by using slicing
>>> numbers = [0, 1, 2, 3, 4, 5, 6]
>>> print(numbers[1:4])
[1, 2, 3]
>>> print(numbers[:3])
[0, 1, 2]
>>> print(numbers[3:])
[3, 4, 5, 6]
>>> [3, 4, 5, 6]
[3, 4, 5, 6]
>>> # len(list): Returns the number of elements in the list.
>>> print(len(numbers))
7
>>> #list.sort(): Sorts the list in ascending order.
>>> numbers.sort()
>>> print(numbers)
[0, 1, 2, 3, 4, 5, 6]
>>> [0, 1, 2, 3, 4, 5, 6]
[0, 1, 2, 3, 4, 5, 6]
>>> # list.reverse(): Reverses the order of the list.
>>> numbers.reverse()
>>> print(numbers)
[6, 5, 4, 3, 2, 1, 0]
>>> [6, 5, 4, 3, 2, 1, 0]
[6, 5, 4, 3, 2, 1, 0]
>>> #list.index(item): Returns the index of the first instance of an item.
>>> print(numbers.index(1))
5
>>> print(numbers)
[6, 5, 4, 3, 2, 1, 0]
>>> [6, 5, 4, 3, 2, 1, 0]
[6, 5, 4, 3, 2, 1, 0]
>>> 
>>> 
>>> #string count
>>> name= "fatima"
>>> print(name.count("a"))
2
