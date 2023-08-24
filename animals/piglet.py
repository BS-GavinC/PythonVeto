from animals.wild import *

class Piglet(Wild):

    def __init__(self, name, race, color, size, dirty) -> None:
        super().__init__(name, race, color, size)
        self.__dirty = dirty

    @property
    def dirty(self):
        return self.__dirty
    
    @dirty.setter
    def dirty(self, value):
        self.__dirty = value

    def make_noise(self):
        super().make_noise()
        print("- Quick Quick nous c'est le gout")

        """permet de manger avec ou sans proprete
        bool : neatly
        """
    def eat(self, neatly):
        print(f"groin groin je me regale {'proprement' if neatly else 'de maniere deguaulasse'}")
        self.dirty = not neatly