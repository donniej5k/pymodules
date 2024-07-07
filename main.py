# 2. Mastering Python Modules and Aliases 
# main.py

import text_utils as tu

def main():
    user_input = input("Enter a string: ")

    reversed_string = tu.reverse_string(user_input)
    capitalized_string = tu.capitalize_string(user_input)

    print(f"Reversed String: {reversed_string}")
    print(f"Capitalized String: {capitalized_string}")

if __name__ == "__main__":
    main()
