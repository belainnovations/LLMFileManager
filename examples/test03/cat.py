from animal import Animal

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, species="Cat", color=color)

    def make_sound(self):
        return "Meow!"

    def scratch(self):
        return f"{self.name} is scratching the furniture!"

    def __str__(self):
        return f"{super().__str__()} with {self.color} fur"