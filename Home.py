class Person:

    def __init__(self):
        self.age = None
        self.name = None

    def set_age(self):
        self.age = 18

    def set_name(self):
        self.name = 'Carol'

    def print_details(self):
        print(f'The name is {self.name} and the age is {self.age}')


def let_us_conflict():
    my_person = Person()
    my_person.set_age()
    my_person.set_name()
    my_person.print_details()


let_us_conflict()
