number_grid = [  # A list of lists
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[2])  # Print the list
print(number_grid[2][1])  # Print the list and the 1 location in it

for row in number_grid:  # Loop to search each list in number_grid
    for col in row:  # Loop to search each value in each list
        print(col)  # Print each col found
