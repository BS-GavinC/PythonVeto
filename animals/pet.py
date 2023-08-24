from animals.animal import *

class Pet(Animal):

    def __init__(self, name, race, color, size, chip_nbr) -> None:
        super().__init__(name, race, color, size)
        self.__chip = chip_nbr

    @property
    def chip(self):
        return self.__chip
    
    @chip.setter
    def chip(self, value):
        self.__chip = value