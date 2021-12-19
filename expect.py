def valueError(a):
    while True:
        try:
            print(a)
            raise ValueError("Oops!  That was no valid number.  Try again...")
            continue
        except ValueError as ve:
            print(ve)
