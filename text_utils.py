# text_utils.py

def reverse_string(s):
    """
    Reverses the given string.
    
    Args:
    s (str): The string to be reversed.
    
    Returns:
    str: The reversed string.
    """
    return s[::-1]

def capitalize_string(s):
    """
    Capitalizes the given string.
    
    Args:
    s (str): The string to be capitalized.
    
    Returns:
    str: The capitalized string.
    """
    return s.capitalize()

if __name__ == "__main__":
    # Test the module directly
    test_string = "hello"
    print(f"Original: {test_string}")
    print(f"Reversed: {reverse_string(test_string)}")
    print(f"Capitalized: {capitalize_string(test_string)}")
