

try:
    number = int(input("Enter a number: "))
    print(number)
except:  # this will show for everything inside the try area
except ZeroDivisionError:  # specific erros
    print("Divided by Zero")
except ValueError:
    print("Invalid Input")
