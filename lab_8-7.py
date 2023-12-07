"""
Create a Python file named lab_8-7.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Using the nested list rows from the "Nested Data" slide, write a function that prints each person's name 
BONUS: Make each name be possessive. Remember, if a name ends in s, only add an apostrophe. If the name does not end in s, add, 's.

"""
#Nicholas Yepes 12/07/23

#creates function
def print_possessive_names(nested_data):
    #loops through data and goes through all data
    for row in nested_data:
        for name in row:
            #checks for s and adds s 
            possessive_name = name + ("'" if name[-1] == 's' else "'s")
            #prints 's to names 
            print(possessive_name)

# names in nested data list
nested_data = [
    ["Darick", "Eugene", "Kyle", "Azaan"],
    ["Ryan", "Phil", "Eman", "Alex", "Nicholas"],
    ["Christian", "Josh", "Matt", "Francesco"],
    ["Patrick", "Nico", "Trevayne"]
]
#prints names 
print_possessive_names(nested_data)