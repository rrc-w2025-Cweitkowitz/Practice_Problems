"""
In this module I will conduct the second set of problems in module 3.

Simple python problems designed to keep my knowledge of Python
up to date.
"""

___author___ = "Connor Weitkowitz"
___version___ = "11/05/2025"

from Module_2_Problems import question_break
import random
import math

def module_3_problems():
    """
    1.  Write a program that generates two random numbers between 0 and 100 
        and prints the smaller of the two numbers.
    """
    number_1 = random.uniform(0, 100)
    number_2 = random.uniform(0, 100)
    min_number = min(number_1,number_2)
    
    print(f"{number_1:,.2f}, {number_2:,.2f}")
    print(f"{min_number:,.2f}")
    print(question_break)
    
    """
    2.  Write a program that takes a float as an input, then computes and outputs
        the cube of that number using the pow method of the math module.
    """
    # Turning into non input for ease of use in rest of program
    float_input = float("30.55")
    
    print(f"Your number is {float_input}")

    cube_input = float_input ** 3
    
    print(f"Your number cubed is {cube_input}")

    """
    3.  Write a program that reads from the keyboard the radius of a circle. 
    Calculate and output the area and the circumference of that circle. 
    You can use the following formulas: math formula goes here haha :3c
    """
    radius = 5
    circumference = 2 * math.pi * radius
    area = math.pi * (5 ** 2)

    print(f"C of a circle is: {circumference:,.2f}\nArea of the circle is: {area:,.2f}")

    """
    4.	Write a program that generates five random integers between 60 and 
    100 and calculates the smallest of the five numbers.
    """



    """
    5.	Write a program that generates three random integers between 0 and 
    50, calculates the average, and prints the result to one decimal place.
    """

module_3_problems()

if __name__ == '__Main__':
    module_3_problems()