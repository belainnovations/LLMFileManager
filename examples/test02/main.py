from animal import Animal
from dog import Dog
from cat import Cat

def main():
    animal = Animal("Generic Animal")
    dog = Dog("Buddy")
    cat = Cat("Whiskers")

    animals = [animal, dog, cat]

    for animal in animals:
        animal.speak()
        animal.move()

    dog.fetch()
    cat.scratch()

if __name__ == "__main__":
    main()