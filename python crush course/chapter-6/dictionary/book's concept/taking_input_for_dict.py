#Empty dictionary.
my_dict = {}
#Numbers of items to add.
n = int(input("How many items do you want to add to the dictionary?"))
#Loop to add items to the dictionary.
for i in range(n):
    key = input("Enter the key:")
    value = input("Enter the value:")
    my_dict[key] = value
#Print the final dictionary.
    print("Final dictionary is:", my_dict)
