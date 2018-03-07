class Player:
    def __init__(self, name):
        self.name = name

    def read_position(self):
        x = int(input("Enter number "))
        y = (input("Enter letter from a to j "))
        return (x, y)
