from animal import Animal

class Dog(Animal):
    def __init__(self, name, breed, color):
        super().__init__(name, species="Dog", color=color)
        self.breed = breed

    def make_sound(self):
        return "Woof!"

    def fetch(self):
        return f"{self.name} is fetching the ball!"

    def __str__(self):
        return f"{super().__str__()} of breed {self.breed}"