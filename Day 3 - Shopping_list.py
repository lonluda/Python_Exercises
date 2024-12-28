# Shopping List
# 
# Create a shopping list app where user can insert,
# remove and read what to buy at Supermarket !
# 
# Github: lonluda

import os
import json

def clean_console():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def load_list():
    if os.path.exists('shopping_list.json'):
        with open('shopping_list.json', 'r') as file:
            return json.load(file)
    return []

def save_list():
    with open('shopping_list.json', 'w') as file:
        json.dump(shopping_list, file)
        print("Shopping list saved !")

def insert_items(shopping_list):
    print("---")
    print("Insert a new item: \n")
    new_item = input("> ")
    if new_item != '':
        if new_item in shopping_list:
            input("You also included this item in your list !")
        else:
            shopping_list.append(new_item)
            save_list()
    else:
        input(f"Insert a value !")

def remove_items(shopping_list):

    if not shopping_list:
        input("Your shopping list is empty! Nothing to remove.")
        return

    print("---")
    print("Insert the index of the item to remove: \n")
    remove_item = input("> ")

    try:
        int_remove_item = int(remove_item)
        shopping_list.pop(int_remove_item - 1) # -1 is for align the n. 0 index with n.1 index
        input("Item removed !")
        save_list()
    except (ValueError, IndexError) as e:
        print(f"You insert a non value input or wrong item index.\n")
        input(f"Please insert only existing numbers !")

def view_items(shopping_list):

    clean_console()

    if not shopping_list:
        input("Your shopping list is currently empty! Add some items to get started.")
    else:
        print("You list include: \n")
        for i,item in enumerate(shopping_list):
            print(f"Object n. {i+1} - {item}")
        input()

def get_numeric_input():
    while True:
        clean_console()
        print(f"Welcome in the Shopping List App!")
        print("What do you want to do ?\n")
        print("1. Insert a new item")
        print("2. Remove an item")
        print("3. View the shopping list")
        print("4. Exit")

        user_input = input("\n>> ")
        if not user_input.strip():  # Se l'utente preme solo Invio
            input("Input non valido! Non puoi lasciare vuoto. Inserisci un numero valido.\n")
            continue
        try:
            user_input = int(user_input)
            if user_input < 1 or user_input > 4:  # Controllo più semplice
                input("Input fuori range! Inserisci un numero tra 1 e 4.\n")
                continue
            return user_input
        except ValueError:
            input("Input non valido! Inserisci solo numeri.\n")

def menu():
    while True:
 
        user_input = get_numeric_input()

        match user_input:
            case 1:
                insert_items(shopping_list)
            case 2:
                remove_items(shopping_list)
            case 3:
                view_items(shopping_list)
            case 4:
                print("\nThank you for using the Shopping List App! Goodbye!")
                break

shopping_list = load_list()

if __name__ == "__main__":
    menu()
