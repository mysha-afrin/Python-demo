def pet_animal(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.\n")
pet_animal('dog', 'bruno')
pet_animal('cat', 'whiskers')

#creating a error by calling the function with different parameters

def pet_animal(animal_type, pet_name):
    '''Display information about a pet.
    '''
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.\n")
pet_animal('bruno', 'dog')



def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person
musician = build_person('jimi', 'hendrix')
print(musician)
