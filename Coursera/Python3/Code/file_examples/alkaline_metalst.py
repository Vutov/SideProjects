'''(data in file) -> list of lists
Write a for loop to read the contents of alkaline_metals.txt and store it in a list
of lists, with each inner list containing the name, atomic number, and
atomic weight for an element.
'''

metal_list = []

with open('alkaline_metals.txt', 'r') as metals:
    for line in metals:
        metal_list += [line.split()]

print ('The list is: ', metal_list)
