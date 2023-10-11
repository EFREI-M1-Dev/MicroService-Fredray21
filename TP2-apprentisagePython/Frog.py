from Animal import Animal

class Frog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.name = "Green frog"

    def jump(self):
        print(f'{self.name} is jumping.')