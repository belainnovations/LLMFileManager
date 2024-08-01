from animal import Animal

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says: Meow!")

    def scratch(self):
        print(f"{self.name} is scratching the furniture.")