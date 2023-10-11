#########################################################
# Tp2 : Apprentissage de Python pour personnes avancées #
# Auteur : Frederic Dabadie                             #
# Date : 11/10/2023                                     #
#########################################################
from Animal import Animal
from Frog import Frog
from Dog import Dog
from Cat import Cat
from Toys import Toys
from PetWithToys import PetWithToys
import time

# Créez une liste d'animaux et d'animaux de compagnie
animalList = [Dog('Milou', 5), Frog('Kermit', 1), Cat('Garfield', 3), Dog('Pluto', 2)]
petList = [PetWithToys('Buddy', 5, 'ball'), PetWithToys('Whiskers', 2, 'feather')]

for animal in animalList:
    animal.eat()
    time.sleep(0.5)
    animal.drink()
    time.sleep(0.5)
    print(f'{animal.name} is {animal.age} years old.')
    time.sleep(0.5)
    if isinstance(animal, Dog): # isinstance() métaclasse
        animal.bark()
    elif isinstance(animal, Frog):
        animal.jump()
    elif isinstance(animal, Cat):
        animal.meow()
    else:
        print("This animal is not recognized.")
    print("")
    time.sleep(0.5)

# affichage suite à l'héritage multiple
print("\nHéritage multiple")
for pet in petList:
    pet.eat()
    time.sleep(0.5)
    pet.play()
    time.sleep(0.5)
    print(f'{pet.name} is {pet.age} years old.')
    time.sleep(0.5)

# Connaître l'ordre d'héritage
if __name__ == '__main__':
    print("\nVoici l'execution du main")
    print(Animal.__mro__)
    print(Frog.__mro__)
    print(Dog.__mro__)
    print(Cat.__mro__)
    print(Toys.__mro__)
    print(PetWithToys.__mro__)




