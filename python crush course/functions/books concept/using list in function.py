def great_users(names):
    """Print a greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
usersnames = ['hannah', 'ty', 'margot']
great_users(usersnames)
