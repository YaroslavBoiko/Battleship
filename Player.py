class Player:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def read_position(self):
        x = input("Enter letter from a to j")
        y = int(input("Enter number "))
        return x, y
