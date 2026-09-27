"""
Calculator Master
A menu-driven Python calculator built with Git and GitHub branching.
"""


def add(a, b):
    """Return the sum of a and b."""
    return round(a + b, 2)


def get_number(prompt):
    """
    Prompt the user for a number, re-prompting on invalid (non-numeric) input.
    """
    while True:
        raw_value = input(prompt).strip()
        try:
            return float(raw_value)
        except ValueError:
            print("Invalid input. Please enter a numeric value (e.g., 3 or 3.5).")


def get_menu_choice():
    """
    Prompt the user for a menu choice (1-5), re-prompting on invalid input.
    """
    valid_choices = {"1", "2", "3", "4", "5"}
    while True:
        choice = input("Enter your choice (1-5): ").strip()
        if choice in valid_choices:
            return choice
        print("Invalid choice. Please select a number from 1 to 5.")


def print_menu():
    """Display the calculator's menu options."""
    print("\n===== Calculator Master =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("==============================")


def main():
    print("Welcome to Calculator Master!")

    while True:
        print_menu()
        choice = get_menu_choice()

        if choice == "5":
            print("Thank you for using Calculator Master. Goodbye!")
            break

        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        try:
            if choice == "1":
                result = add(num1, num2)
                symbol = "+"
                print(f"\nResult: {num1} {symbol} {num2} = {result}")
        except ZeroDivisionError as error:
            print(f"\nError: {error}")

        again = input("\nWould you like to perform another calculation? (y/n): ").strip().lower()
        if again != "y":
            print("Thank you for using Calculator Master. Goodbye!")
            break


if __name__ == "__main__":
    main()