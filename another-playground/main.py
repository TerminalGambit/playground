# playing around with python whilst offline

class Vehicle:
    def __init__(self, number_of_wheels: int, color: str, brand: str, environment: str):
        self.number_of_wheels = number_of_wheels
        self.color = color
        self.brand = brand
        self.name: str = None
        self.is_public_transport: bool = True
        self.environment: str = environment

    def set_name(self, name: str):
        self.name = name

class Bike(Vehicle):
    def __init__(self, number_of_wheels: int, color: str, amount_of_gears_front: int, amount_of_gears_rear: int, brand: str):
        super().__init__(number_of_wheels, color, brand, environment="land")
        self.amount_of_gears_front = amount_of_gears_front
        self.amount_of_gears_rear = amount_of_gears_rear
        self.current_gear_front = amount_of_gears_front
        self.current_gear_rear = amount_of_gears_rear

    def up_shift_front(self):
        if self.current_gear_front < self.amount_of_gears_front:
            self.current_gear_front += 1
        else:
            self.current_gear_front = self.amount_of_gears_front

    def up_shift_rear(self):
        if self.current_gear_rear < self.amount_of_gears_rear:
            self.current_gear_rear += 1
        else:
            self.current_gear_rear = self.amount_of_gears_rear

class Car(Vehicle):
    def __init__(self, number_of_wheels: int, color: str, type_of_car: str, brand: str, model: str):
        super().__init__(number_of_wheels, color, brand, environment="land")
        self.number_of_wheels = number_of_wheels
        self.color = color
        self.type_of_car = type_of_car
        self.brand = brand
        self.model = model
