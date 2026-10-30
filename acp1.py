
class Pet:
    def __init__(self, name, animal_type, age, color):
        self.name = name
        self.animal_type = animal_type
        self.age = age
        self.color = color

    def display_profile(self):
        print("----- Pet Profile -----")
        print("Pet Name:", self.name)
        print("Animal Type:", self.animal_type)
        print("Age:", self.age, "years")
        print("Color:", self.color)


# Creating pet objects
pet1 = Pet("Buddy", "Dog", 3, "Brown")
pet2 = Pet("Whiskers", "Cat", 2, "White")
pet3 = Pet("Coco", "Parrot", 1, "Green")

# Displaying pet profiles
pet1.display_profile()
pet2.display_profile()
pet3.display_profile()
