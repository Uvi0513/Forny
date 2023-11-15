#!/usr/bin/env python
import re

def calculate(expression):
    try:
        return eval(expression)
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print("Simple Calculator for Termux")
    print("Enter a mathematical expression (e.g., 5 + 3, 10 * 2, 15 / 3)")

    user_input = input("Enter your problem: ")

    # Check for invalid characters in the input
    if not re.match("^[\d\s\.\+\-\*/\(\)]+$", user_input):
        print("Invalid characters in the input. Please enter a valid expression.")
        exit(1)

    result = calculate(user_input)
    print(f"Result: {result}")
