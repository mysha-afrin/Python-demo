class dog:
    "A simple attempt to define a dog."
    def __init__(self, name, age):
        "Initialize name and ahe attribute."
        self.name = name
        self.age = age
    def sit(self):
        """Simulates a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
    def roll_over(self):
        '''Simulates rolling over in response to a command'''
        print(f"{self.name} rolled over.")
