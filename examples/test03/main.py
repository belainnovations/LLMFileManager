from animal import Animal
from dog import Dog
from cat import Cat

def main():
    # Create instances of each class
    generic_animal = Animal("Generic", "Unknown")
    buddy = Dog("Muddy", "Golden Retriever")
    whiskers = Cat("Whiskers", "Tabby")

    # Demonstrate the use of common methods
    print(generic_animal)
    print(buddy)
    print(whiskers)

    print("\nMaking sounds:")
    print(f"{generic_animal.name}: {generic_animal.make_sound()}")
    print(f"{buddy.name}: {buddy.make_sound()}")
    print(f"{whiskers.name}: {whiskers.make_sound()}")

    # Demonstrate specific methods
    print("\nSpecific actions:")
    print(buddy.fetch())
    print(whiskers.scratch())

    # Demonstrate polymorphism
    animals = [generic_animal, buddy, whiskers]
    print("\nPolymorphism example:")
    for animal in animals:
        print(f"{animal.name} says: {animal.make_sound()}")

if __name__ == "__main__":
    main()