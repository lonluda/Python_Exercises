# Calculator program
# Github: lonluda
# Second exercise of the Python course

import os

def clean():
    if os.name == 'posix':
        os.system("clear") 
    else:
        os.system("cls")

def main():
    print("Welcome to the calculator program!")

    while True:
        print("Insert 'exit' for close the program.")
        first_number = input("\nEnter the first number:\n > ")
        if first_number == "exit":
            break
        second_number = input("\nEnter the second number:\n > ")
        if second_number == "exit":
            break
        operation = input("\nEnter the operation: \n'+' for Sum\n'-' for Subtraction\n'*' for Multiplication\n'/' for Division\n > ")
        if operation == "exit":
            break
        
        try:
            int_first_number = int(first_number)
            int_second_number = int(second_number)
            clean()
            match operation:
                case "+":
                    print(f"The result of the sum is: {int_first_number + int_second_number}")

                case "-":
                    print(f"The result of the subtraction is: {int_first_number - int_second_number}")
                case "*":
                    print(f"The result of the multiplication is: {int_first_number * int_second_number}")
                case "/":
                    if int_second_number == 0:
                        print("You can't divide by zero!")
                        continue
                    print(f"The result of the division is: {int_first_number / int_second_number}")
                case _:
                    print("Invalid operation, try again.")
            continue

        except ValueError:
            print("Please enter only valid number !")

if __name__ == "__main__":
    main()
