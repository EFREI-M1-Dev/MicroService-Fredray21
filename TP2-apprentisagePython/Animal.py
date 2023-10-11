class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name} is eating.')

    def drink(self):
        print(f'{self.name} is drinking.')