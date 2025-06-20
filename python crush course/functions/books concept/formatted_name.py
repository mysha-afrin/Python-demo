def get_formatted_name(first_name, last_name):
    """Return a full namel, nearly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrik')
print(musician)



def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a formatted full name, with an optional middle name."""
    full_name = f"{first_name} {middle_name} {last_name}".title()
    return full_name
musician = get_formatted_name("jimi", "hendrix", "lee")
print(musician)



def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
