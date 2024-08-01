from animal import Animal

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says: Woof!")

    def fetch(self):
        print(f"{self.name} is fetching the ball.")