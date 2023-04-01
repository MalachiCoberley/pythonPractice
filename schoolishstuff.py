"""
Question 1
You are given data about five areas of the world with their
corresponding territories as follows:
• Afghanistan = 93
• Albania = 355
• Algeria = 213
• Andorra = 376
• Angola = 244
• Antarctica = 672
How would you store this information in two separate Python lists?
"""

countries = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antarctica']
territories = [93, 355, 213, 376, 244, 672]

"""
Question 2
How would you store the two lists from Question 1 into a single Python
dictionary?
After creating the Python dictionary, can you print all of its information
into the Python console?
Use the following format example for each of the elements in your lists
for your Python console output:
The area of Afghanistan is 93
"""
dic = {}
for a, b in enumerate(countries):
    dic[b] = territories[a]



"""
Question 3
Lets say now you want to classify the areas of the world, in the
dictionary created in Question 2, according to whether its areas are
greater than 300.
How would you script your solution so your Python console output
would be as follows:
Areas less or equal than 300: ['Afghanistan', 'Algeria', 'Angola’]
Areas greater than 300: ['Albania', 'Andorra', 'Antarctica']
"""

 

"""
Question 4
Given the following Python script, what would be the console output?
Explain your rationale.
lsta = [1,1,2,3,3]
lstb = [2,3,3,4,5]
print(lsta + lstb)
print(set(lsta))
print(set(lstb))
print(set(lsta) & set(lstb))
print(set(lsta) | set(lstb))
Question 5
Can you create a Python script that outputs to the console all the even
numbers larger than 24 and less than 128 in a list?
Question 6
Can you get the length of each of the strings in the Python list below
into a new list only using one line of code?
lsta = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antarctica']
Question 7
Print a dictionary that takes Fahrenheit as keys and Celsius as values
from 10 to and including 100 using only one line of code. Then use a
print statement to print the dictionary. Here are a couple of formulas
that may be useful for this task:
# Fahrenheit to Celsius Conversion = (Fahrenheit - 32) * (5/9)
# Celsius to Fahrenheit Conversion = (Celsius * (9/5)) + 32
Question 8
Can you migrate the following Python comprehension statement into a
regular script statement with multiple lines? Please note that both the
comprehension and regular script will have the same Python Console output.
lsta = [(1,4,7), (2,5,8), (3,6,9)]
a = sorted([i for each in lsta for i in each])
print(a)
Python Console Output:
[1, 2, 3, 4, 5, 6, 7, 8, 9]
Question 9
Create a Python function that takes a positive integer as a parameter,
then the function will calculate the sum of all numbers in its range
starting from zero by default?
For instance, if the range is 101, the number will be 5050
Question 10
Create a Python lambda function that computes the area of a square
with a length denoted using m as its argument name.
Question 11
True or False Statement:
Given the following Python script, the Python console output is 10
b = None
def fun1():
global b
b = 10
fun1()
print(b)
Question 12
Finish the incomplete code below, that takes as user input the radius of a given circle, then
computes the circumference and area of the given circle.
Your solution needs to have one function named circumference that takes as an input the radius of
a circle and returns the circumference. Then you will need to create a lambda function that
computes the area of the circle. At the end you will print the circumference(using the function) and
area of the circle (using the lambda function), having each result rounded to 3 decimals.
import math
r = float(input('Enter the radius of your circle: '))
pi = math.pi
### place your code below this line
### place your code above this line
"""
