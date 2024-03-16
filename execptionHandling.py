# exception = events detected during execution that interrupts the flow
# of the program
try:
    numerator = int(input("Enter a number to divide:"))
    denominator = int(input("Enter a number to divide by:"))
    result = numerator/denominator
    # print(result)
except ZeroDivisionError as e:
    # we do this only to display what kind of exception occurred too
    print(e)
    print("You cannot divide by zero idiot!")
except ValueError as e:
    print(e)
    print("Please Enter a number idiot!")
except Exception as e:
    print(e)
    print("Something Went Wrong!")
else:
    # only if no exceptions occur
    print(result)

# whether we catch an exception or not this block of code
# will run

finally:
    print("This will always execute!")

