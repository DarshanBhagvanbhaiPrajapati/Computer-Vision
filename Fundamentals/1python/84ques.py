#lab9:multi level inheritence animal hirarchy
class Animal:
    def __init__(self, species):
        self.species = species

    def display_species(self):
        print("Species:", self.species)

class Mammal(Animal):
    def __init__(self, species, diet):
        super().__init__(species)
        self.diet = diet

    def display_info(self):
        super().display_species()
        print("Diet:", self.diet)

class Carnivore(Mammal):
    def __init__(self, species, diet, hunting_method):
        super().__init__(species, diet)
        self.hunting_method = hunting_method

    def display_info(self):
        super().display_info()
        print("Hunting Method:", self.hunting_method)

lion = Carnivore("Lion", "Meat", "Predatory")

lion.display_info()
