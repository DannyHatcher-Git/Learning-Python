def decorator_function(original_fucntion):  # First function
    def wrapper_function():  # second function
        return original_fucntion()
    return wrapper_function


def display():  # function called display
    print("display function ran")


decorated_display = decorator_function(display)  # make a variable = a function

decorated_display()  # run this variable

# .......... EXAMPLE..........


def decorator_function(original_fucntion):  # First function
    def wrapper_function():  # second function
        print("wrapper executed this before {}".format(
            original_fucntion.__name__))
        return original_fucntion()
    return wrapper_function


@decorator_function  # This is the same as the line below
# decorated_display = decorator_function(display)  # make a variable = a function
def display():  # function called display
    print("display function ran")


def display_info(name, age):
    print("display_info ran with arguments ({}, {}".format(name, age))

# display()  # run this variable
