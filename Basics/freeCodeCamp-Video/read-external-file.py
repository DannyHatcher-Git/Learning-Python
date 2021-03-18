'''
open("file location", "r")  # read mode
open("file location", "W")  # write mode (overwrite existing or make new file)
open("file location", "a")  # append mode (add text at the end)
open("file location", "r+")  # read and write mode
'''

readme_file = open("readme.md", "r")
print(readme_file.readable())  # Can I read the file
print(readme_file.read())  # Read the file contents
# Read the first line and puts cursor on second line (can be repeated)
print(readme_file.readline())
# puts lines in list and can be indexed for reference
print(readme_file.readlines())


readme_file.close()
