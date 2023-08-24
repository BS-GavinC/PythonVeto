from animals.pet import *

class Cat(Pet):

    def __init__(self, name, race, color, size, chip_nbr, is_aggressive) -> None:
        super().__init__(name, race, color, size, chip_nbr)
        self.__is_aggressive = is_aggressive

    @property
    def aggressive(self):
        return self.__is_aggressive
    
    @aggressive.setter
    def aggressive(self, value):
        self.__is_aggressive = value

    def make_noise(self):
        super().make_noise()
        print("- miouuuw miouuuw")

    def sleep(self):
        print("rompiiiiche rompiiiiche")