
class Animal:

    def __init__(self, name, race, color, size) -> None:
        self.__name = name
        self.__race = race
        self.__color = color
        self.__size = size

    @property
    def name(self):
        return self.__name
    
    @property
    def race(self):
        return self.__race
    
    @property
    def color(self):
        return self.__color
    
    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        self.__size = value

    @color.setter
    def color(self, value):
        self.__color = value

    @name.setter
    def name(self, value):
        self.__name = value

    def make_noise(self):
        print(f"{self.name} : ")