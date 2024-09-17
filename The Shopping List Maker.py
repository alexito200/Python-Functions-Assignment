# Objective: The aim of this assignment is to create a program that helps users make a shopping list.

# Task 1: Write a function that lets the user add items to a list.

shopping_list = []

def user_shopping_list():
    while True:
        adding_items = input("what items would you like to add: ")
        if adding_items.lower() == "done":
            break
        shopping_list.append(adding_items)

# Task 2: Include a function to remove items from the list.

def shopping_list_removal(shopping_list):
    removing_items = input("what item would you like to remove: ")
    if removing_items in shopping_list:
        shopping_list.remove(removing_items)

# Task 3: Add a function that prints out the entire list in a formatted way.

def formatted_list(shopping_list, dash="-"):
    if shopping_list:
        print(f"Here is your updated shopping list:")
        for item in shopping_list:
            print(f"{dash} {item}")
    else:
        print("Your shopping list is empty")


user_shopping_list()
shopping_list_removal(shopping_list)
formatted_list(shopping_list)

# Note: The goal of this is to be a program. The recommendation is to use a while loop that will allow the user to continue to
# add, remove, and print off their shopping list until they decide to "quit", also known as breaking the loop.