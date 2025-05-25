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
import statistics

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
    print(question_break)


    """
    3.  Write a program that reads from the keyboard the radius of a circle. 
    Calculate and output the area and the circumference of that circle. 
    You can use the following formulas: math formula goes here haha :3c
    """
    radius = 5
    circumference = 2 * math.pi * radius
    area = math.pi * (5 ** 2)

    print(f"C of a circle is: {circumference:,.2f}\nArea of the circle is: {area:,.2f}")
    print(question_break)
    
    
    """
    4.	Write a program that generates five random integers between 60 and 
    100 and calculates the smallest of the five numbers.
    """
    number_list = []

    for number in range(0, 5):
        rng = random.randint(60, 100)
        number_list.append(rng)
        sorted_numbers = sorted(number_list)
        print(f"Number list is {number_list}")
        print(f"Sorted number list is{sorted_numbers}")
        print(f"Lowest number is {sorted_numbers[0]}")
        print(question_break)


    """
    5.	Write a program that generates three random integers between 0 
    and 50, calculates the average, and prints the result to one decimal 
    place.
    """
    num_list = []
    for number in range(0, 3):
        rng3 = random.randint(0, 50)
        num_list.append(rng3)
    
    print(f"Your random numbers are: {num_list}")
    print(f"The mean of the number is: {statistics.mean(num_list):,.2f}")
    print(question_break)


    """
    6. Write a program that takes two integers as input from the 
    keyboard, representing the number of hits and the number of at-bats 
    for a batter. Then calculate the batters hitting percentage and 
    check if the hitting percentage is above .300. If it is, output that 
    the player is eligible for the All Stars Game; otherwise, output 
    that the player is not eligible.
    """
# input("Please enter your total number of hits: ")
# input("Please enter your total number of bats: ")
    total_number_of_hits = 5000
    total_number_of_bats = 25
    batting_average = int(total_number_of_hits) / int(total_number_of_bats)
    
    print(f"Your total number of hits are: {total_number_of_hits}\n"
          f"Your total number of bats is: {total_number_of_bats}\n"
          f"Your batting average is {batting_average}")
    if batting_average < .300:
        print("Im sorry but you are not eligable for all star status :(")
    else:
        print("YaaaY!!! you are an all star now, just like that guy who did " 
              "the thing with a baseball!!")
    print(question_break)
    

    """
    7.	Write a program that reads a single char as an input from the 
        keyboard and outputs whether it is a valid character to start a 
        variable identifier.
    """
    # input("Enter a character to check if it can be a variable: ")
    char_check = "R"

    for character in char_check:
        if character.isalpha:
            print(f"Yes you can use {char_check} as a varaible.")
        else:
            print(f"No, you cannot use {char_check} as a variable.")

    print(question_break)

    """
    8.	Write a program that reads a sentence from the keyboard. 
        Depending on the last character of the sentence, print a 
        message identifying the sentence as declarative (ends with 
        a period), interrogative (ends with a question mark), 
        exclamatory (ends with an exclamation point), or other.
    """
    sentence = "What is the air speed velocity of an unladen swallow?"
    sen_end = sentence[-1]
    special_char = [".", "?", "!"]
    
    for char in special_char:
        if sen_end == char:
            if sen_end == special_char[0]:
                print("This sentence is declarative.")
            elif sen_end == special_char[1]:
                print("This sentence is interrogative?")
            elif sen_end == special_char[2]:
                print("This sentence is exclamatory!")
            elif sen_end != special_char:
                print("This sentence is other.")
    
    print(question_break)
    
    
    """
    9.	An email address contains the @ character. Write a program 
        that takes a word from the keyboard and outputs whether it is an 
        email address based on the presence of the @ character. Do not 
        worry about what else is in the word.
    """
    email = "DavidTheGnome@gnomemail.com"
    email_valid = "@"
    
    for letter in email:
        if letter == email_valid:
            print("This is a valid email address")

    """
    10.	Write a program that takes two words as input from the 
    keyboard, representing a password and the same password again. 
    (Often, websites ask users to type their password twice when they 
    register to make sure there was no typo the first time around.) 
    Your program should do the following:
    
    if both passwords match, then output "You are now registered as a
    new user"
    otherwise, output "Sorry, there is a typo in your password"
    """
    # input("Please create a password: ")
    password_input = print("Bababooey")
    # input("Please re-type your password to verify i: ")
    password_verify = print("Bababooey")

    if password_input == password_verify:
        print("You are now registered as a new user")
    elif password_input != password_verify:
        print("Sorry, there is a typo in your password")

    print(question_break)

    """
    11.	Write a program that takes a word as input from the keyboard, 
    representing a user ID. (Often, websites place constraints on user 
    IDs.) Your program should do the following:

    if the user ID contains between 6 and 10 characters inclusive, then 
    output "Welcome, barbara" (assuming barbara is the user ID entered)
    otherwise, output "Sorry, user ID invalid"
    """
    # input("Please enter your user id: ").lower()
    user_id = "BarbAra".lower()
    correct_user_id = "barbara"

    if user_id == correct_user_id and range(6,11):
        print("Welcome, Barbara")
    
    elif user_id != range(6,11) or correct_user_id:
        print("Incorrect user id length and user id.")

    




    
    """
    12.	Write a program that reads a web address (for instance, 
    www.yahoo.com) from the keyboard and outputs whether this web 
    address is for a government, a university, a business, an 
    organization, or another entity.

    If the web address ends with gov, it is a government web address
    If the web address ends with edu, it is a university web address
    If the web address ends with com, it is a business web address
    If the web address ends with org, it is an organization web address
    Otherwise, it is a web address for another entity
    """

    """
    13.	Write a program that reads a temperature as a whole number 
    from the keyboard and outputs a "probable" season (winter, spring, 
    summer, or fall) depending on the temperature.

    If the temperature is greater than or equal to 90, it is probably 
    summer.
	If the temperature is greater than or equal to 70 and less than 90, 
    it is probably spring.
	If the temperature is greater than or equal to 50 and less than 70, 
    it is probably fall.
	If the temperature is less than 50, it is probably winter.
	If the temperature is greater than 110 or less than −5, then you 
    should output that the temperature entered is outside the valid range.
    """

module_3_problems()

if __name__ == '__Main__':
    module_3_problems()