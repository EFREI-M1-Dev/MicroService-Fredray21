from Animal import Animal
from Toys import Toys

class PetWithToys(Animal, Toys):
    def __init__(self, name, age, toy_name):
        Animal.__init__(self, name, age)
        Toys.__init__(self, toy_name)