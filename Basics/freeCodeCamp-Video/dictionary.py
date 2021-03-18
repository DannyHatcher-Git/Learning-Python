monthConverstions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}
# The keys can be numbers as well as strings
print(monthConverstions["Dec"])
# Has to be square bracket for a direct reference
print(monthConverstions.get("Oct", "Not a valid option"))
# Use .get to allow for a default error message
print(monthConverstions.get("oct", "Not a valid option"))
# Use .get to allow for a default error message (in this case the o is not capitalised)
