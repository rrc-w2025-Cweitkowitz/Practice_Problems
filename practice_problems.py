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
"""
savings_account = 5039.32
