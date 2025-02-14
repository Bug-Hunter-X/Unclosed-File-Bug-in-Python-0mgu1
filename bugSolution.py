import os

def function_with_closed_file(filename):
    try:
        with open(filename, 'w') as f:
            # ... some code that might raise an exception ...
            f.write('Some text')
            1/0 # Simulate an exception
    except ZeroDivisionError:
        print("Exception handled correctly")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        if os.path.exists(filename):
            print(f"File '{filename}' exists")

function_with_closed_file("my_file.txt") # run function