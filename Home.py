class Person:

    def __init__(self):
        self.age = None
        self.name = None

    def set_age(self, age):
        self.age = age

    def set_name(self, name):
        self.name = name

    def print_details(self):
        print(f'The name is {self.name} and the age is {self.age}')


def let_us_conflict(age, name):
    my_person = Person()
    my_person.set_age(age)
    my_person.set_name(name)
    my_person.print_details()


let_us_conflict(21, 'Nobody')
