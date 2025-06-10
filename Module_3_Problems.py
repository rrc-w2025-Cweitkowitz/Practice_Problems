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

    print(question_break)
    
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
    # input("Please enter a web adress: ")
    web_address_input = "www.Firefox.com"
    VALID_WEB = [".gov", ".edu", ".com", ".org"]
    web_address_check = web_address_input[-4:]

    if web_address_input == VALID_WEB[0]:
        print("This is a government web address.")

    
    elif web_address_check == VALID_WEB[1]:
        print("This is a university web address.")

    
    elif web_address_check == VALID_WEB[2]:
        print("This is a buisness web address.")

    
    elif web_address_check == VALID_WEB[3]:
        print("This is an organization web address.")

    
    elif web_address_check not in VALID_WEB:
        print("This web address is from somewhere else.")

    print(question_break)

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
    # input(Please enter a temperature in farenheit: )
    temp_check = 75
    VALID_RANGE = range(-6, 111)

    if temp_check in VALID_RANGE:
        if temp_check >= 90:
            print("Probably summer.")
        if temp_check >= 70 < 90:
            print("probably spring.")
        if temp_check >= 50 < 70:
            print("Probably fall.")
        if temp_check < 50:
            print("Probably Winter.")
    else:
        print("Temperature not in valid range.")

    print(question_break)
    
    """
    14.Write a program that takes a string as an input from the 
    keyboard, representing a year. Your program should do the 
    following.

    If the year entered has two characters, convert it to an integer,
        add 2000 to it, and output it.
    If the year entered has four characters, just convert it to an
        integer and output it.
    If the year entered neither has two nor four charcters, output
        that the year is not valid.
    """
    # input("Please enter a year, any year: ")
    year_input = "2023"
    
    # Adds 20 to a two digit string input, to turn it into a year.
    year_adder = "20"
    year_loop_active = True

    while year_loop_active == True:
    
        # Checks length of converted input to check 
        # if it needs additonal numbers
        if len(year_input) == 2:
            complete_year = year_adder + year_input
            complete_year_int = int(complete_year)
            print(int(complete_year_int))
            year_loop_active = False
        
        elif len(year_input) == 4:
            year_int = int(year_input)
            print(year_int)
            year_loop_active = False

        elif len(year_input) != 2 or 4:
            print("Year entered is non-valid, please enter 2 or 4 " \
            "numbers to continue")
            year_loop_active = False
    print(question_break)
    

    """
    15. Write a program that takes two words as input from the keyboard
    ,representing a user ID and a password. Your program should do the 
    following.

    If the user ID and the password match "admin" and "open", 
        respectively, then output "Welcome."
    If the user ID mathces "admin" and the password does not match
        "open", output "Wrong password."
    If the password matches "open" and the user ID does not match 
        "admin", output "Wrong user ID."
    Otherwise, output "Sorry, wrong ID and password."
    """
    account_info = {
        "Account name": "dmin",
        "Password" : "open"
    }
    # input("Please enter your account name: ")
    acct_name_input = "admin"
    # input("Please enter your password: ")
    acct_pword_input = "open"
    acct_loop = True
    
    # Activates the loop and ensures it will not loop infinitely
    while acct_loop == True:    
        
        # Checks dictionary for proper ID and p-word
        if acct_name_input in account_info["Account name"] \
            and acct_pword_input in account_info["Password"]:
            print("Welcome.")
            acct_loop = False
        
        # Catches incorrect Password used for acct_info
        if acct_name_input in account_info["Account name"] and \
            acct_pword_input not in account_info["Password"]:
                print("Wrong password.")
                acct_loop = False
        
        # Catches incorrect ID but correct password used
        if acct_name_input not in account_info["Account name"] and \
            acct_pword_input in account_info["Password"]:
                print("Wrong used ID.")
                acct_loop = False
        
        # catches both ID and p-word inputs beign incorrect
        if acct_name_input not in account_info["Account name"] and \
            acct_pword_input not in account_info["Password"]:
            print("Sorry, wrong ID and password.")
            acct_loop = False

    print(question_break)
    
    """
    16.	Write a program that prompts the user for a value greater than 
    10 as an input (you should loop until the user enters a valid 
    value) and finds the square root of that number and the square root 
    of the result, and continues to find the square root of the result 
    until you reach a number that is smaller than 1.01. The program 
    should output how many times the square root operation was 
    performed.
    """
    # input("Please enter a value greater then 10: ")
    number_input = 11
    
    # Loops until a number greater then 10 is chosen
    while int(number_input) <= 10:
        
        # input("Enter a number greater then 10: ")
        number_reinput = 11
        number_input = number_reinput
    
    # Only runs if a number greater then 10 is chosen.
    # Turns teh int into a float to square and prints the result
    # Result is also turned into a square, rounded to 2 decimal places
    if int(number_input) > 10:
        input_sqrt = math.sqrt(float(number_input))
        print("Results will be rounded to 2 decimals.")
        print(f"{input_sqrt:.2f}")
        print(f"{math.sqrt(input_sqrt):.2f}")

    print(question_break)
    
    """
    17.	Write a program that expects a word containing the @ character 
    as an input. If the word does not contain an @ character, then your 
    program should keep prompting the user for a word. When the user 
    types in a word containing an @ character, the program should simply 
    print the word and terminate.
    """

    # input("Please enter a word with an @ symbol: ")
    at_input = "@"
    at_loop = True

    while at_loop == True:
            # Checking input for an @ symbol and iterating until one is found
            if "@" not in at_input:
                re_input = input("Word must contain an @ symbol: ")
                at_input = re_input
            # Once an @ is detected, the word is printed and loop terminates
            else:
                print(at_input)
                at_loop = False

    print(question_break)

    """
    18.	Write a program that reads float values from a file named 
    input.txt and outputs the average.
    """
    floats = []
    with open("input.txt", "r") as file:
        for file_float in file:
            float_strip = file_float.strip()
            float_num = float(float_strip)
            floats.append(float_num)
        # gets average by adding all the numbers and dividing them
        # by the length of the list
        average = sum(floats) / len(floats)
        print(average)

        print(question_break)
    """
    19.	Write a program that uses a for loop to output the sum of all 
    the integers between 10 and 20, inclusive, that 
    is, 10 + 11 +12 + ... + 19 + 20.
    """
    num_range = []
    # iterates through a range of numbers from 10 to 20
    # Appends to the num_range list
    for number in range(10, 21):
        num_range.append(number)
        # Prints sum of all numbers in list once finished appending
        # via a hard stop at the end.
        if len(num_range) == 11:
            print(sum(num_range))

    print(question_break)

    """
    20. Write a program that uses a for loop to output the product of 
    all the integers between 3 and 7, inclusive, that is, 3*4*5*6*7
    """
    for number in range(3,7):
        multi = number * (number + 1) 
        print(multi)

    print(question_break)

    """
    21. Write a program that uses a for loop to count how many 
    multiples of 7 are between 33 and 97, inclusive.
    """

    seven_mult_count = 0
    
    # Iterates through number 33 to 97 looing for any multiples of seven
    for number in range(33, 97):
        
        # Divides each number by seven
        seven_mult = number / 7
        
        # Checks each divison for whole numbers and increases the counter
        # Tracking multiples of seven by one
        if seven_mult.is_integer():
            seven_mult_count += 1

    print(seven_mult_count)
            
    print(question_break)

    """
    22. Write a program that reads an integer value from the user and
    outputs Hello World the number of times entered by the user. Verify
    that the user has entered an integer. If the input is 3, the output
    will be Hello World printed three times.
    """
    # int_input = input("Please enter a number: ")
    int_cast = 3
    int_count = 0
    loop_active = True
    
    while loop_active == True:
        #if not int_input.isnumeric:
            #int_input("Please enter a number: ")
        
        # prints Hello World and increases counter each iteration
        if int_cast != int_count:
            print("Hello World.")
            int_count += 1
        
        # stops the print once the count equals the number input
        if int_cast == int_count:
            loop_active == False
module_3_problems()

if __name__ == '__Main__':
    module_3_problems()