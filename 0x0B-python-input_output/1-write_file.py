#!/usr/bin/python3
def write_file(filename="", text=""):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            char_count = file.write(text)
            return char_count
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return 0  # Return 0 characters written in case of an error
