# This code defines a function that prints a message about a shirt size and a message on it.
# It then calls the function twice with different arguments.
def make_shirt(size, message):
    print(f"\nIf the shirt size is {size}, then the message on the shirt will be {message.title()}.")
make_shirt('large', 'I love Python')
make_shirt('medium', 'Python is awesome')
