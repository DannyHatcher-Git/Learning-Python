print("Write first number symbol second number and seporate with space")
incalc = input("")  # Asking for the calcuation

outcalc = incalc.split(" ")
# splitting the incalc stuff (using space " " ) and making the result outcalc

num1 = float(outcalc[0])
symbol = outcalc[1]
num2 = float(outcalc[2])

# could replace if with elif in the latter part
if symbol == "-":
    print(num1 - num2)
elif symbol == "+":
    print(num1+num2)
elif symbol == "/":
    print(num1/num2)
elif symbol == "*":
    print(num1*num2)
