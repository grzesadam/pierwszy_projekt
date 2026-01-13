"""
Main script for pierwszy_projekt
This script can be run directly in PyCharm.
"""


def greet(name):
    """
    Returns a greeting message.
    
    Args:
        name (str): The name to greet
        
    Returns:
        str: A greeting message
    """
    return f"Hello, {name}!"


def main():
    """
    Main function that executes when the script is run.
    """
    print("Welcome to pierwszy_projekt!")
    print("=" * 50)
    
    # Get user input
    user_name = input("Please enter your name: ")
    
    # Display greeting
    greeting = greet(user_name)
    print(greeting)
    
    # Simple calculation example
    print("\nLet's do a simple calculation:")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 + num2
        print(f"The sum of {num1} and {num2} is: {result}")
    except ValueError:
        print("Error: Please enter valid numbers!")
    
    print("\n" + "=" * 50)
    print("Thank you for using pierwszy_projekt!")


if __name__ == "__main__":
    main()
