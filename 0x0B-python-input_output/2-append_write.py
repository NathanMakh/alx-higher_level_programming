def append_write(filename="", text=""):
    try:
        with open(filename, 'a', encoding='utf-8') as file:
            char_count = file.write(text)
            return char_count
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return 0  # Return 0 characters added in case of an error
