import random as rd


class Ship:
    def __init__(self, length):
        self.__length = length
        self.__hit = [False] * length
        self.coordinate = self.generate_ship([1, 12 - length], length)
        self.horizontal = self.is_horizontal()
        self.bow = self.coordinate[0]

    def shoot_at(self, tuple):
        try:
            self.__hit[self.coordinate.index(tuple)] = True
            return True
        except ValueError:
            return False

    def get_hit(self):
        return self.__hit

    def generate_ship(self, limits, length):

        coordinate = []
        abc = "abcdefghij"

        way = int(rd.uniform(0, 2))
        head_x = int(rd.uniform(limits[0], limits[1]))
        head_y = int(rd.uniform(limits[0], limits[1]))

        if way == 0:
            for i in range(length):
                coordinate.append((abc[head_y], head_x + i))
        else:
            for i in range(length - 1):
                coordinate.append((abc[head_y + i], head_x))
        return (coordinate, way)

    def is_horizontal(self):

        if self.coordinate[1] == 0:
            return True
        else:
            return False
