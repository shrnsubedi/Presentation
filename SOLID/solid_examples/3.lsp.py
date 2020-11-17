
'''
L: Liskov Substitution Principle

Objects in a program should be replaceable with instances of their base types without altering the correctness of that program.

The Liskov Substitution Principle basically states that any subclass should be replaceable with its parent class.
'''

class Vehicle:

   def __init__(self, name: str, speed: float):
       self.name = name
       self.speed = speed

   def get_name(self) -> str:
       return f"The vehicle name {self.name}"

   def get_speed(self) -> str:
       return f"The vehicle speed {self.speed}"

   def start_movement(self):
       self.movement_start()

class VehicleWithEgine(Vehicle):
    def engine(self):
       pass

    def start_movement(self):
       self.movement_start()


class VehicleWithoutEngine(Vehicle):
    def start_movement(self):
        self.movement_start()

class Car(VehicleWithEgine):
   def start_movement(self):
       pass

class Bicycle(VehicleWithoutEngine):
   def start_movement(self):
       pass

------------->