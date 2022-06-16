class Member:
    def __init__(self, name: str):
        self.name = name
        self.nr_friends = 0
        self.price = 0 

    def print_name(self):
        print(self.name)
