from animals.pet import *


class Dog(Pet):

    def __init__(self, name, race, color, size, chip_nbr, ball_nbr) -> None:
        super().__init__(name, race, color, size, chip_nbr)
        self.__ball_nbr = ball_nbr

    @property
    def ball_nbr(self):
        return self.__ball_nbr
    
    @ball_nbr.setter
    def ball_nbr(self, value):
        self.__ball_nbr = value

    def make_noise(self):
        super().make_noise()
        print("- uwuf uwuf")

    def sit(self):
        print(f"{self.name} s'est assis")