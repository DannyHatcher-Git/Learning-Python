def outer_function():
    message = "HI"

    def inner_function():
        print(message)
    return inner_function()  # with () it returns hi


outer_function()


def outer_function(msg):  # first fuction
    def inner_function():  # second function
        print(msg)  # print from first function
    return inner_function  # make inner_function work


hi_func = outer_function("Hi")  # make a new variable
bye_func = outer_function("Bye")  # make a new variable

hi_func()  # do this function
bye_func()  # do this function
