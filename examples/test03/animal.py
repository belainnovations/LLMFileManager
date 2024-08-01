class Animal:
    def __init__(self, name, species, color):
        self.name = name
        self.species = species
        self.color = color

    def make_sound(self):
        return "Some generic animal sound"

    def __str__(self):
        return f"{self.name} is a {self.species}"