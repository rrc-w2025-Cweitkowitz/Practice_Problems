"""
In this module I will conduct the first SDF practice problems found in 
module 2.

Simple python problems designed to keep my knowledge of Python
up to date.
"""

___author___ = "Connor Weitkowitz"
___version___ = "09/05/2025"

"""
Given the following variables with corresponding values:
name = "Jo-Anne Sinclair"
salary = 123093
1. Define a print statement that will produce the following output:
Jo-Anne Sinclair: 123093
2. Use an f-string to produce the following output:
Name: Jo-Anne Sinclair
Salary: $123,093.00

"""
question_break = print("\n************************\n")

# 1. Define a print statement that will produce the following output:
#    Jo-Anne Sinclair: 123093
print("Jo-Anne Sinclair: 123093")

question_break

name = "Jo-Anne Sinclair"
salary = 123093

print(f"Name: {name}\nSalary: {salary:,.2f}")

question_break

"""
1.	Declare a variable to store the balance of a savings account. 
    The current balance is 5039.32.Use a meaningful variable name 
    and proper naming conventions.

2. 	Declare a second variable to store the above value as an 
    integer. Use type-casting on the above variable to achieve 
    this. Use a meaningful variable name and proper naming conventions.

3.	Print each variable keeping in mind the formatting of the output 
    as shown below: Editors note: I did not get the format woopsie haha. 
"""
savings_account = 5039.32
integer_savings_account = int(savings_account)

print(f"Savings Account Raw Data:{savings_account}\nSavings Account:$ "
      f"{integer_savings_account:,.2f}")

question_break

"""
4.	Write a program that uses a list of tuples, where each tuple 
    contains the name flower item and its corresponding cost. Print 
    the list of tuples.
ex. [('carnation', 1.79), ('tulip', 0.77), ('rose', 3.99), 
    ('iris', 0.89)]
"""

flower_list = [('carnation', 1.79), ('tulip', 0.77), ('rose', 3.99), 
               ('iris', 0.89)]

question_break

"""
5.	Add a list of dictionaries. Each dictionary will have two key-value 
    pairs. The keys will be "name" and "flower" while the values will be 
    a person's actual name, and the name of their favorite flower. Print 
    the list of dictionaries.
"""

[{'name': 'Alice', 'flower': 'carnation'}, {'name': 'Fred', 'flower': 'Iris'}, 
 {'name': 'Dave', 'flower': 'tulip'}, {'name': 'Jerry', 'flower': 'rose'},]

question_break

"""
6.	Add two sets each with values of your choice. Print a new set 
    containing only the values that appear in both.
"""
heirloom_warframes = {'Frost', 'Mag', 'Ember', 'Rhino'}
prime_warframes = {'Excalibur', 'Volt', 'Ember', 'Saryn', 'Rhino', 'Hildryn'}
warframe_intersection = heirloom_warframes.intersection(prime_warframes)

print(warframe_intersection)