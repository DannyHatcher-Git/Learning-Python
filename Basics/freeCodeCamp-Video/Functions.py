def say_hi():  # def needed for a function
    print("Hello")


print("1", "Top")
say_hi()  # Need to call a functions and will go up to recall the fucntions
print("3", "Bottom")


def sayhi(name):
    print("Hello" + name)


sayhi(" Chris")
sayhi(" Danny")


def sayhello(name, age):
    print("Hello " + name + ", you are " + str(age))


sayhello("Sara", 30)
sayhello("Tia", 70)


def cube(num):
    return num*num*num  # Make sure the calculation has something to print
# Can't type code underneeth the return command


print("8", cube(3))
