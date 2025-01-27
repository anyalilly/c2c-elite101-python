
"""
    Welcome to Elite 101 this program is a starter for your chatbot project.
    The starter prompts the user to enter their name and then greets them with a personalized message.

    Functions:
        get_user_name(): Prompts the user to enter their name and returns it.
        greet_user(name): Prints a greeting message using the provided name.
        main(): Main function that orchestrates the user input and greeting process.

    Execution:
        When the script is run directly (not imported as a module), it will execute the main() function.
"""

import sys 
def get_user_age():
    return int(input("Please enter your age: "))

def get_user_name():
    return input("Please enter your name: ")

def greet_user(name):
    print(f"Hello, {name}, welcome to the school lunch line!")

def main():
    user_name = get_user_name()
    greet_user(user_name)
    user_age = get_user_age()
    if user_age <= 10:
        print('Okay, continue to the elemnatary school interface.')
    elif 11 <= user_age <= 14:
        print('Okay, continue to the middle school interface.')
    elif 15 <= user_age <=18: 
        print('Okay, continue to the high school interface.')
    else:
        print("Error, please enter an age between 3-18.")
        get_user_age()

    print()


if __name__ == "__main__":
    main()


def end_program():
    print('Thank you for using this program.')
    sys.exit(0)

def display_menu():
    print('What would you like for me to do for you today? Look at the menu below and choose an option.')
    print()
    print('School Lunch Menu')
    print('1: View the Schedule of the Week')
    print("2: View Today's Meal")
    print('3: Submit a Complaint')
    print('4: Ask a question')
    print('5: Exit Program')
    print()

def user_selection():
  global isUsed
  user_choice = int(input("Enter a number between 1-5: "))
  if user_choice == 1:
    print('Schedule of the Week')
  elif user_choice == 2:
    print("View Today's Meal")
  elif user_choice == 3:
    print("Submit a Complaint")
  elif user_choice == 4:
    print("Ask a Question")
  elif user_choice == 5:
    print("Thank you for using the program!")
    isUsed = False
    sys.exit(0) # https://www.freecodecamp.org/news/python-exit-how-to-use-an-exit-function-in-python-to-stop-a-program/, exiting program
  else:
    print("Error message.")


display_menu()
user_selection()

