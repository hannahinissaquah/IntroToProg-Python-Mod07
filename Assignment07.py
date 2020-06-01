# ------------------------------------------------- #
# Title: Assignment07
# Description: My Son's Reading Log
# ChangeLog: (Who, When, What)
# HChung, 5.29.2020, Added Pseudo-Code
# HChung, 5.30.2020, Created Script
# HChung, 5.30.2020, Added Structured Error-Handling
# ------------------------------------------------- #

import pickle  # This imports code from another code file!

# Data -------------------------------------------- #
strFileName = 'ReadingLog.dat'
lstTable = []
strChild = "Eddie"

# Processing -------------------------------------- #

class CustomError(Exception):
    """ Value must be entered """
    def __str__(self):
        return "Value was not entered."

def manage_file(file_name, mode, list_of_data = None): # list_of_data is optional because if in 'read' mode, don't want ot pass any data
    """ A custom wrapper function for the standard open() file function

    :param list_of_data: (string) with data to save
    :param file_name: (string) with name of file
    :param mode: (string) with name of mode [Write, Overwrite, Read]
    :return: (string) with data or write/append status
    """

    if mode.lower() == 'write':
        with open(file_name, "ab") as file: # store the list object into a binary file
            pickle.dump(list_of_data, file)
            return "New data added to file!"
        # automatically closes file
    elif mode.lower() == 'overwrite': # store the list object into a binary file
        with open(file_name, "wb") as file:
            list_of_data = ["Book", "Minutes"]
            pickle.dump(list_of_data, file)
            return "File overwritten and new data added to file!"
    elif mode.lower() == 'read': # Read the data from the file into a new list object and display the contents
        with open(file_name, "rb") as file:
            print(strChild+'\'s Reading Log:')
            list_of_data = [] # declare variable outside of while loop
            while True:
                try:
                    list_of_data.append(pickle.load(file))
                except EOFError: # End of File Error
                    break
            return list_of_data
    else:
        print('No matching mode option')

# Presentation ------------------------------------ #

print("\n--------------- Welcome " + strChild+ "! ---------------")

while(True):
    print('''
    What would you like to do?
        1 = Display Your Reading Log
        2 = Add To Your Reading Log
        3 = Create a New Log or Overwrite the Log
        4 = Exit
        ''')

    choice = input('Enter an Option: ')
    print() # add a new line for looks
    if choice == '1':
        try:
            print(manage_file(file_name=strFileName, mode='read'))
        except FileNotFoundError as e:
            print("Oops! File not found!")
            print("Tip: You can select Option 2 or 3 to start a New Reading Log.\n")
            print("The Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print("There as a non-specific error!")
    elif choice == '2': # Get Book and Minutes Read From user, then store it in a list object
        while True:
            try:
                strBook = str(input("Enter the Name of the Book: "))
                if len(strBook) == 0:
                    raise CustomError()
                intTime = int(input("Enter the Minutes You Read: "))
                lstTable = [strBook, intTime]
                manage_file(file_name=strFileName, mode='write', list_of_data=lstTable)
                break
            except ValueError:
                print("\nOops! That was not a number. Please try again!\n")
            except Exception as e:
                print("There was a non-specific error!")
                print("The Built-In Python error info: ")
                print(e, e.__doc__, type(e), sep='\n')
    elif choice == '3':
        manage_file(file_name=strFileName, mode='overwrite')
    elif choice == "4":
        print("Great Job, "+strChild+"! Keep it up!")
        input("Press the Enter key to Exit")
        break
    else:
        print('Please Enter Choice 1, 2, 3, or 4!')