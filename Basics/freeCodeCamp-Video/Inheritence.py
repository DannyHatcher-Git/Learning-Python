class Chef:
    def make_chicken(self):
        print("The chef makes a chicken")

    def make_salad(self):
        print("The chef makes salad")

    def make_special_dish(self):
        print("The chef makes the special dish")


# copy all the things in the Chef class in here (duplicate) Things can be made again for overwriting.
class SpecialChef(Chef):
    def make_special(self):
        print("The chef makes special")


myChef = Chef()
myChef.make_chicken()  # Must put brackets on the end for a function to work
