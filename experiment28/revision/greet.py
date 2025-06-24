def greet_user():
    "Display a simple greeting."
    print("Hello world")
greet_user()



def greet_user(username):
    print(f"Hello,{username.title()}")
greet_user("jeba")


#passing a information in function
def greet_user(username):
    """Display a simple greeting ."""
    print(f"Hello,{username.title()}")
greet_user("mysha afrin")
greet_user("jinia afrin")
#qn no-1 solved
def display_message(message):
    print(message)
display_message("I am learing python")


#qn no-2 solved
def fav_book(book):
    print(f"My favorite book is {book.title()}")
fav_book("Alice in wander land")


#Display multiple parametre in a function
def fav_pet(pet_name, pet_type, my_name):
    print(f"\nMy name is {my_name.title()}.")
    print(f"I have a {pet_type}.")
    print(f"My {pet_type}'s name is {pet_name.title()}.\n")
fav_pet("ginger", "dog", "jeba")
fav_pet("cinamon", "cat", "pial")



#qn no-3 solved
def make_shirt(size, quote):
    print(f"\nThe size of the tshirt is {size}.")
    print(f"Write '{quote}' on it.\n")
make_shirt(input("Enter the size: "), input("What should I write on it? "))



#qn no-4 solved
def make_shirt(size, quote):
    print(f"\nThe size of the tshirt is {size}.")
    print(f"Write '{quote}' on it.\n")
make_shirt("XL", "I love python.")
make_shirt("M", "Coding is love.")
make_shirt("S", "Coding is my life")





