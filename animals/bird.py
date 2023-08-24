from animals.wild import *


class Bird(Wild):

    def __init__(self, name, race, color, size, vocabulary) -> None:
        super().__init__(name, race, color, size)
        self.__vocabulary = vocabulary

    @property
    def vocabulary(self):
        return self.__vocabulary
    
    @vocabulary.setter
    def vocabulary(self, value):
        self.__vocabulary = value

    def make_noise(self):
        super().make_noise()
        print(f"- {self.vocabulary[0]}")

    def fly(self):
        print(f"Ohlalala ! {self.name} est entrain de voler !")