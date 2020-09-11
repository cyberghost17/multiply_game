# version 01
import random
import os
try:
    import PIL

except ImportError:
    os.system('pip install pillow')
    import PIL

try:
    import requests # don't worry about error

except:
    os.system('pip3 install requests')
    import requests
# lists

main_list = [' 2 * 1', '2 * 2', '2 * 3', '2 * 4', '2 * 5', '2 * 6', '2 * 7', '2 * 8', '2 * 9', '2 * 10', '2 * 11', '2 * 12']
correct_list = []
wrong_list = []

# lists
def update_program (): 
    pass

def main_program ():
    print('---------- Multiply Game ----------')

    while True:
        current_equation = random.choice(main_list) # this is for picking a str out of main list
        user_answer = input(str(current_equation) + ': ')
        # catch any error's in string 

        if user_answer == '':
            user_answer = '0'

        try:
            user_answer = int(user_answer)

        except:
            user_answer = '0'

        # find if answers match
        parsed_equation = current_equation.split()
        first_number = int(parsed_equation[0])
        second_number = int(parsed_equation[2])

        correct_answer = first_number * second_number

        if int(user_answer) == int(correct_answer):
            print('Correct answer! =)\n')
            correct_list.append(current_equation)

        else:
            print('WORNG!!!...')
            print('Correct answer was: ' + str(correct_answer) + '\n')
            wrong_list.append(current_equation)

        # delete equation from main list
        main_list.remove(current_equation)

    # return and analyze the results

def email_manager ():
    pass

main_program()