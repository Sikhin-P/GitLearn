class Person:

    def __init__(self):
        self.age = None
        self.name = None

    def set_age(self):
        self.age = 18

    def set_name(self):
        self.name = 'Carol'

    def print_details(self):
        print(f'The name is : {self.name}')
        print(f'The age is : {self.age}')
