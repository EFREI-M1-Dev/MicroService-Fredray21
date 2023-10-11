from Animal import Animal

class Dog(Animal):
    def bark(self):
        print(f'{self.name} is barking.')

    def eat(self):  # Surcharge d'une fonction
        print(f'{self.name} is eating meat.')