
# Parent class
class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def display_info(self):
        print("Brand:", self.brand)
        print("Color:", self.color)

    def start(self):
        print("The vehicle is starting!")


# Child class
class Car(Vehicle):
    def __init__(self, brand, color, model):
        super().__init__(brand, color)
        self.model = model

    # Overriding the parent method
    def start(self):
        print("The car is starting with a key!")

    def display_car(self):
        self.display_info()
        print("Model:", self.model)


# Creating an object
my_car = Car("Toyota", "White", "Innova")

# Displaying car details
my_car.display_car()

# Calling the overridden method
my_car.start()

# Checking inheritance
print("Is Car a subclass of Vehicle?", issubclass(Car, Vehicle))
