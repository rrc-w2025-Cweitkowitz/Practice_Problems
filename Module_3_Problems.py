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
    int_cast = 3 #int(int_input)
    int_count = 0

    while int_cast != int_count:
        #if not int_input.isnumeric:
            #int_input("Please enter a number: ")
        
        print("Hello World.")
        int_count += 1
    
    # stops the print once the count equals the number input
        if int_cast == int_count:
            print(question_break)

    """
    23. Write a program that takes a word as an input from the keyboard
    and outputs each character in the word, seperated by a space.
    """
    # word_input = input("Please enter a word: ")
    word_input = "Cheese"
    #Holding space value 
    seperator = " "
    
    # Empty list to hold letters
    letter_list = []
    
    # Appends each letter to the list
    for letter in word_input:
        letter_list.append(letter)
    
    #Joins each letter in the list to one string and prints a space after each list item
    print(seperator.join(letter_list))

    print(question_break)
    """
    24. Write a program that takes an integer value as an input from the
    keyboard and outputs the factorial of that number; the facotrial of
    an integer n is n * (n − 1) * (n − 2)

    EX: For instance, the factorial of 4 is 4 * 3 * 2 * 1, or 24
    """

    #num_input = input("Please enter an integer value: ")
    num_input = 4
    fact_int = int(num_input)
    fact_counter = fact_int - 1
    fact_loop = True
    
    while fact_loop == True:
        num_input
        
        # Calculation of a factorial that will work with any user input so long as its an integer
        # Does the first calculation, makes the fact_int equal the number, reduced counter by one
        # and loops until counter equals zero (otherwise the whole number will be zero).
        if fact_counter != 0:
            factorial = fact_int * fact_counter
            fact_int = factorial
            fact_counter -= 1
        
        # Triggers upon last factorial multiplication, stops loop and prints factorial result.
        if fact_counter == 1:
            fact_loop = False
            print(factorial)

    print(question_break)
        
    """
    25. Using a loop, write a program that reads 10 integer values from
    the keyboard and outputs the minimum value of all the values entered.
    """

    #int_list = []
    #int_counter = 10
    
    # appends an int type casted input to an empty list until 10 numbers are added
    # while int_counter != 10:
        # int_range_input = int(input("Please enter 10 integer values: "))
        # int_list.append(int_range_input)
        # int_counter += 1
    
    # Grabs smallest number and prints it
    # if int_counter == 10:
    #    int_list_min = min(int_list)
    #    print(int_list_min)
    
    print(question_break)
    
    """
    26.	Write a program that inputs a word representing a binary number 
    (0s and 1s). First, your program should verify that it is indeed a 
    binary number, that is, the number contains only 0s and 1s. If that 
    is not the case, your program should print a message that the 
    number is not a valid binary number. Then, your program should 
    count how many 1s are in that word and output the count.
    """
    #binary_input = (input("Please enter a binary word."))
    binary_input = "1010101"
    zero_count = 0
    one_count = 0
    binary_count = 0

    for number in binary_input:
        # Checks entire binary input for anything not a 0 or a 1.
        if binary_input != "0" or "1":
            print("Input MUST be a binary (0 and or 1)")

        # Adds to variable counter tracking number of zeros.
        if number is "0":    
            zero_count += 1
        
        # Adds to variable counter tracking number of ones.
        if number is "1":    
            one_count += 1
    # Once the result is finalized it prints the total number of zeros and ones, increases the counter
    # by one to ensure it only prints once.
    if binary_count == 0:
        print(f"Your word has {zero_count} many zeros and {one_count} many ones.")
        binary_count += 1
    
    print(question_break)

    """
    27.	Create a copy of the previous problem and update it with the 
    following modification: If the word does not represent a valid binary 
    number, the program should keep prompting the user for a new word 
    until a word representing a valid binary number is input by the user.
    """
    # Binaries_input = input("Please enter a binary number: ")
    binaries_input = "1010101"
    zero_counter = 0
    one_counter = 0
    binary_check = True
    
    for number in binaries_input:

        if number == "0":
            zero_counter += 1
            binary_check == True

        elif number == "1":
            one_counter += 1
            binary_check == True

        elif number is not "0" or "1":
            zero_counter == 0
            one_counter == 0
            binary_check == False
            binaries_reinput = input("Word MUST be a binary! ")
            binaries_input == binaries_reinput
    
    if binary_check == True:
        print(f"Your word has {zero_counter} zeros and {one_counter} ones!")
    
    print(question_break)

    """
    28.	Write a program that inputs a word representing a binary number 
    (0s and 1s). First, your program should check that it is indeed a 
    binary number, that is, the number contains only 0s and 1s. If that is 
    not the case, your program should output that the number is not a valid 
    binary number. If that word contains exactly two 1s, your program should 
    output that that word is "accepted," otherwise that it is "rejected."
    """
    #two_binary_input = (input("Please enter a binary word: "))
    two_binary_input = "11"
    binary_check = True
    two_binary_one_counter = 0

    
    for number in two_binary_input :

        if binary_check is True and number in two_binary_input is "1":

                 
            if binary_check is True and number == "1":
                two_binary_one_counter += 1 

            
            elif binary_check is True and two_binary_one_counter == 2:
                print("This is an acceptable word.")
            
            else:
                print("Too many ones, the acceptable amount of ones is two.")
        
        elif number != "1":
            print("This is not a valid binary number.")
            binary_check == False
    """
    29.	Create a copy of the previous problem and update it with the 
    following modification: If the word does not represent a valid binary 
    number, the program should keep prompting the user for a new word until 
    a word representing a valid binary number is input by the user.
    """

    q29_binary_input = input("Please enter a binary number: ")
    q29_binary_check = True
    q29_binary_one_counter = 0

    
    for number in q29_binary_input:

       
        
        if q29_binary_check is True and number in q29_binary_input is "1":
                q29_binary_one_counter += 1 

                if q29_binary_check is True and q29_binary_one_counter == 2:
                    print("This is an acceptable word.")
            
                else:
                    print("Too many ones, the acceptable amount of ones is two.")
                    q29_binary_check_instance = False
                    q29_binary_check = q29_binary_check_instance
        
        if number != "1":
            print("This is not a valid binary number.")
            q29_binary_check = False
    if binary_check == False:
            q29_re_input = input("Please enter a valid binary response: ")
            q29_binary_input = q29_re_input
            print("test")
        
    

    """
    30.	Write a program that inputs a word representing a binary number 
    (0s and 1s). First, your program should check that it is indeed a 
    binary number, that is, that it contains only 0s and 1s. If that is 
    not the case, your program should output that the number is not a valid 
    binary number. If that word contains at least three consecutive 1s, your 
    program should output that that word is "accepted," otherwise that it 
    is "rejected."
    """


    """
    31.	Write a program that inputs 7 float values from a file dja.txt that 
    represent the Dow Jones Average for 7 days. Your program should output 
    the lowest value for those 7 days and the number of the day on which the 
    lowest value occurred. For this program, instead of setting the initial 
    minimum value to the first value in the file, use the maximum value for 
    a float (sys.float_info.max). Be sure to handle the case of the file 
    being empty.
    """


    """
    32.	Write a program that takes website names as keyboard input until the 
    user types the word stop and counts how many of the website names are 
    commercial website names (i.e., end with .com), then outputs that 
    count. The input of the word stop should be case insensitive.
    """

    """
    33.	Using a loop, write a program that takes 10 values representing 
    exam grades (between 0 and 100) from the keyboard and outputs the 
    minimum value, maximum value, and average value of all the values 
    entered. Your program should not accept values less than 0 or greater 
    than 100.
    """


module_3_problems()

if __name__ == '__Main__':
    module_3_problems()