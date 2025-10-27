#!/usr/bin/env python3
"""
Even or Odd Checker
A simple program to determine if a number is even or odd.
"""

def is_even(number):
    """
    Check if a number is even.
    
    Args:
        number (int): The number to check
    
    Returns:
        bool: True if the number is even, False otherwise
    """
    return number % 2 == 0

def check_even_odd(number):
    """
    Determine if a number is even or odd and return a descriptive string.
    
    Args:
        number (int): The number to check
    
    Returns:
        str: A message indicating whether the number is even or odd
    """
    if is_even(number):
        return f"{number} is an even number"
    else:
        return f"{number} is an odd number"

if __name__ == "__main__":
    # Test the function with various numbers
    test_numbers = [0, 1, 2, 10, 15, 42, 99, 100]
    
    print("Even/Odd Checker")
    print("=" * 30)
    
    for num in test_numbers:
        result = check_even_odd(num)
        print(result)
    
    # Interactive mode
    print("\n" + "=" * 30)
    print("Try it yourself!")
    try:
        user_input = int(input("Enter a number: "))
        print(check_even_odd(user_input))
    except ValueError:
        print("Please enter a valid integer.")
