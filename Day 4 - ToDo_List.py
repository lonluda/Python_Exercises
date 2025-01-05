# ToDo APP
# github: lonluda
# Version 0.1
#

import os
import json
import datetime

import tabulate

"/* CONSTANTS AND VARIABLES */"

VERSION = 0.1
MEMO_ARCHIVE = 'todo_data.json'
INDEX_ARCHIVE = 'index.json'
DEBUG = True
PRIORITY_CAPTION = {
    0: "Normal",
    1: "Important",
    2: "Urgent",
}

date = datetime.date.today()
items_index = None
todo_list = []

"/* GENERIC METHODS */"

def log(message: str):
    """Print and error message if DEBUG is enabled."""
    if DEBUG:
        input(f"[DEBUG] {message}")

def clean_console() -> None:
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

"/* LOAD FILES METHODS */"

def load_memo_file() -> object:
    try:
        with open(MEMO_ARCHIVE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        log(f"No stored data. A new archive will be created. - {e}")
        save_memo_file(todo_list)
    return []

def save_memo_file(todo_list: list) -> None:
    try:
        with open(MEMO_ARCHIVE, 'w') as file:
            json.dump(todo_list, file)
    except (Exception, json.JSONDecodeError) as e:
        log(f"Something went wrong while saving the memo file. - {e}")

def load_index_file() -> object:
    try:
        with open(INDEX_ARCHIVE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        log(f"No stored data. A new index file will be created. - {e}")

def save_index_file(items_index: int) -> None:
    try:
        with open(INDEX_ARCHIVE, 'w') as file:
            json.dump(items_index, file)
    except (Exception, json.JSONDecodeError) as e:
        input(f"Something went wrong while saving the index file. - {e}")

"/* APP SPECIFIC METHODS */"

def print_menu(todo_list: list) -> None:
    while True:
        clean_console()
        print(f"Welcome in ToDo APP - {VERSION}\n")
        print("What do you want to do ?\n")
        print("1. View List")
        print("2. Add Item")
        print("3. Remove Item")
        print("4. Exit")
        user_input = input("\n> ")

        try:
            int_user = int(user_input)
            if int_user == 1:
                view_list(todo_list)
                input()
            elif int_user == 2:
                add_item(todo_list)
            elif int_user == 3:
                remove_item(todo_list)
            elif int_user == 4:
                exit()
            else:
                input(f"An error in menu selection occurred. Please insert only value from 1 to 4")
                continue
        
        except ValueError as e:
            input("Insert only numeric value ! No letters or special caracters are allowed.")
            continue

def view_list(todo_list: list) -> None:
    load_memo_file()
    clean_console()
    if len(todo_list) == 0:
        print("You've not still inserted any to-do item !")
        return
    else:        
        header = todo_list[0].keys()
        rows =  [x.values() for x in todo_list]
        print(tabulate.tabulate(rows, header))

def add_item(todo_list: list) -> None:
    clean_console()

    item = {
        "ID": None,
        "Priority": None,
        "Deadline": None,
        "Name": None,
    }

    try:
        print(f"Insert memo:")
        input_name = input("> ")
        if len(input_name) < 100 and len(input_name) > 0 and input_name.strip() != "":

            print(f"\nInsert memo priority:")
            print("0. Normal - 1. Important - 2. Urgent")
            input_priority = input("> ")
            try:
                input_priority = int(input_priority)

                if input_priority in (0,1,2):
                    print(f"\nInsert the memo deadline:")
                    print("Enter the date in YYYY-MM-DD format\n")
                    input_deadline = input("> ")

                    try:
                        year, month, day = map(int, input_deadline.split('-'))
                        date1 = datetime.date(year, month, day)
                        if date1 >= date:
                            new_index = (int(load_index_file()) + 1)
                            item["ID"] = new_index
                            item["Priority"] = input_priority
                            item["Deadline"] = str(date1)
                            item["Name"] = input_name

                            todo_list.append(item)
                            save_memo_file(todo_list)
                            save_index_file(new_index)
                        else:
                            input(f"Insert a date greater than the current one {date}!")

                    except ValueError as e:
                        input(f"Insert only valid date in YYYY-MM-DD format ! - {e}")
                else:
                    input("Insert only a value between 0 and 2 !")
            except TypeError as e:
                input(f"Insert only numeric value ! - {e}")
        else:
            input("Insert a memo with a length between 1 and 50 characters !")
    except (ValueError, TypeError) as e:
        input(f"An error occurred - {e}")

def remove_item(todo_list: list) -> None:

    clean_console()

    if todo_list:
        view_list(todo_list)
        print("\nInsert the ID of the item you want to remove:")
        item_to_remove = input("> ")

        try:
            item_to_remove = int(item_to_remove)
    
            for item in todo_list:
                if item["ID"] == item_to_remove:
                    todo_list.pop(todo_list.index(item))

            save_memo_file(todo_list)

        except (ValueError, TypeError) as e:
            log(f"Insert only numeric value ! - {e}")
    else:
        input("You've not still inserted any memo !")

def main():
    """ Main method

    Read the configuration file and pass stored data 
    to relative View/Add/Remove menu function.
    """

    todo_list = load_memo_file()
    print_menu(todo_list)

"/* ENTRY POINT */"

if __name__ == "__main__":
    main()
