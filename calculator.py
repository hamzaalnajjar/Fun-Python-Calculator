import random
import time

# this will print text in random colors
def colorful_print(text):
    colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m']
    reset_color = '\033[0m'
    print(random.choice(colors) + text + reset_color)

# this will load animation 
def loading_animation():
    for i in range(3):
        print(".", end='', flush=True)
        time.sleep(0.5)
    print()

# math operations
def add(a, b):
    result = a + b
    colorful_print(f"The result of {a} + {b} is {result}. That's math magic!")
    return result

def subtract(a, b):
    result = a - b
    colorful_print(f"{a} - {b} = {result}. Math sorcery at its finest!")
    return result

def multiply(a, b):
    result = a * b
    colorful_print(f"{a} * {b} = {result}. Multiplied like a pro!")
    return result

def divide(a, b):
    if b == 0:
        colorful_print("Dividing by zero?! That's a big NO-NO! 🛑")
        return None
    result = a / b
    colorful_print(f"{a} ÷ {b} = {result:.2f}. Divide and conquer!")
    return result

def power(a, b):
    result = a ** b
    colorful_print(f"{a} ^ {b} = {result}. Power moves only! ⚡️")
    return result

# should display the menu at beginning 
def get_user_choice():
    print("\n--- 🧮 Fun Python Calculator 🧮 ---")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (x)")
    print("4. Division (÷)")
    print("5. Exponentiation (^)")
    print("6. Exit")
    try:
        choice = int(input("Choose an operation (1-6): "))
        if 1 <= choice <= 6:
            return choice
        else:
            colorful_print("Invalid choice! Try again.")
            return get_user_choice()
    except ValueError:
        colorful_print("Please enter a number from 1 to 6.")
        return get_user_choice()

# will take numbers from the user
def get_numbers():
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        return a, b
    except ValueError:
        colorful_print("Oops! Please enter valid numbers.")
        return get_numbers()

# this is a main loop to run the calculator
def main():
    colorful_print("🎉 Welcome to the Fun Python Calculator! 🎉")
    while True:
        choice = get_user_choice()
        
        if choice == 6:
            colorful_print("Thanks for using the Fun Python Calculator! See you next time! 🚀")
            break

        a, b = get_numbers()

        colorful_print("Crunching the numbers... 🧪")
        loading_animation()

        if choice == 1:
            add(a, b)
        elif choice == 2:
            subtract(a, b)
        elif choice == 3:
            multiply(a, b)
        elif choice == 4:
            divide(a, b)
        elif choice == 5:
            power(a, b)

        colorful_print("\nWant to do another calculation? Let's gooo! 🚀\n")

if __name__ == "__main__":
    main()
