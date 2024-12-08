def function_with_closed_file(filename):
    try:
        f = open(filename, 'r')
        # ... some code that processes the file ...
    finally:
        f.close()  # Ensure the file is closed in all cases
    return