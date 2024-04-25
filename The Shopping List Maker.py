#Task 1:


def add_item(shopping_list, item):
    shopping_list.append(item)
    print(f"{item} has been added to the shopping list.")




#Task 2:


def remove_item(shopping_list, item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} has been removd from the shopping list.")
    else:
        print(f"{item} is not in the shopping list.")




#Task 3:


def print_list(shopping_list):
    if shopping_list:
        print("Shopping List:")
        for index, item in enumerate(shopping_list, start=1):
            print(f"{index}. {item}")
    else:
        print("Your shopping list is empty.")

my_shopping_list = []

add_item(my_shopping_list, "Bread")
add_item(my_shopping_list, "Cookies")
add_item(my_shopping_list, "Milk")

print_list(my_shopping_list)

remove_item(my_shopping_list, "Cookies")

print_list(my_shopping_list)

