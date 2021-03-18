def raise_to_power(base_num, power_num):
    result = 1  # Where the result is stored
    for x in range(power_num):
        # Loop through the power num - 1 so if it is ^2 it will go through the loop once
        result = result * base_num  # The new result = the old result * the base_num
    return result  # return the finished reslut


print(raise_to_power(2, 5))  # The calculation being asked and printed
