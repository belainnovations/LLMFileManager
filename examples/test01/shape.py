class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def describe(self):
        return f"I am a {self.color} shape."