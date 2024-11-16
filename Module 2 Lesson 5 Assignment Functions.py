#1. The Calculator App

def add(x, y):
    """Adds two numbers."""
    return x + y

def subtract(x, y):
    """Subtracts two numbers."""
    return x - y

def multiply(x, y):
    """Multiplies two numbers."""
    return x * y

def divide(x, y):
    """Divides two numbers."""
    if y == 0:
        return "Division by zero!"
    return x / y

while True:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice(1/2/3/4/5): ")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
    elif choice == '5':
        break
    else:
        print("Invalid input. Please enter a number between 1 and 5.")

# 2. The Shopping List Maker

def add_item(shopping_list):
    item = input("Enter item to add: ")
    shopping_list.append(item)

def remove_item(shopping_list):
    item = input("Enter item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
    else:
        print(f"{item} not found in the list.")

def print_list(shopping_list):
    print("\nShopping List:")
    if not shopping_list:
        print("Your shopping list is empty.")
    else:
        for i, item in enumerate(shopping_list):
            print(f"{i+1}. {item}")

shopping_list = ["apples", "bananas", "carrots", "dates"]

while True:
    print("\nMenu:")
    print("1. Add item")
    print("2. Remove item")
    print("3. Print list")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_item(shopping_list)
    elif choice == "2":
        remove_item(shopping_list)
    elif choice == "3":
        print_list(shopping_list)
    elif choice == "4":
        break
    else:
        print("Invalid choice.")