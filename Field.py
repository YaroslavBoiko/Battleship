import Ship as S


class Field:

    def __init__(self):
        # self.__data = self.make_field()
        self.__ships = ()
        self.field_without = self.make_field()
        self.field_with = self.make_field()

    def field_without_ship(self):
        i = 0
        for ship in self.__ships:
            if True in ship.get_hit():
                for damage in ship.get_hit():
                    if damage == True:
                        tuple = ship.coordinate[0][i]
                        self.draw(self.field_without, tuple, 'X')
            i += 1

    def draw(self, field, tuple, char):
        for row in field:
            if row[0] == tuple[0]:
                if tuple[1] != 10:
                    row = row[:tuple[1]] + char + row[tuple[1]:]
                else:
                    row = row[:tuple[1]] + char

    def generate_field(self):
        boats = []
        for i in range(4):
            c = 0
            len = 4 - i
            count = 5 - len
            boat = S.Ship(len)
            while True:
                ship = boat.generate_ship([1, 12 - len], len)
                build = True
                area = self.no_ship(ship, len)
                for row in area:
                    for el in row:
                        print("el",el)
                        print("row",row)
                        if self.has_ship(el):
                            build = False
                if build:
                    boats.append(boat)
                    c += 1
                if c == count:
                    break
                print("boat is",boats)
        return boats

    def no_ship(self, coordinate, len):
        abc = "abcdefghij"
        area = []

        # if str(coordinate)[0][1] == coordinate[-1][1]:
        #     area = self.x_area(abc, coordinate)
        # else:
        print(coordinate)
        print(coordinate[0][0])
        if coordinate[0][0][0] in abc[1:-len]:
            if coordinate[0][0][1] > 1 and coordinate[-1] < 10:
                start = abc.index(coordinate[0][0][0]) - 1
                end = abc.index(coordinate[0][-1][0]) + 2
                number = coordinate[0][0][1] - 1

                for i in range(3):
                    l = [(letter, number) for letter in abc[start: end]]
                    number += 1
                    area.append(l)
            else:
                start = abc.index(coordinate[0][0][0]) - 1
                end = abc.index(coordinate[0][-1][0]) + 1
                number = coordinate[0][0][1]

                for i in range(2):
                    l = [(letter, number) for letter in abc[start: end]]
                    if coordinate[0][0][1] == 1:
                        number += 1
                    else:
                        number -= 1
                    area.append(l)
        else:
            if coordinate[0][0][1] > 1 and coordinate[0][-1][1] < 10:
                start = abc.index(coordinate[0][0][0]) - 1
                end = abc.index(coordinate[0][-1][0])
                number = coordinate[0][0][1] - 1

                for i in range(3):
                    l = [(letter, number) for letter in abc[start: end]]
                    number += 1
                    area.append(l)
            else:
                number = coordinate[0][0][1]
                if coordinate[0][0][1] == 1:
                    start = abc.index(coordinate[0][0][0])
                    end = abc.index(coordinate[0][-1][0]) + 2
                else:
                    start = abc.index(coordinate[0][0][0])
                    end = abc.index(coordinate[0][-1][0]) + 2
                    number = coordinate[0][0][1]

                for i in range(2):
                    l = [(letter, number) for letter in abc[start:end]]
                    if coordinate[0][0][1] == 1:
                        number += 1
                    else:
                        number -= 1
                    area.append(l)
        return area

    def has_ship(self, tuple):
        for ship in self.__ships:
            if tuple in ship:
                return True
        return False
        # if "*"not in data[tuple[0]]:
        #     return False
        # else:
        #     if data[tuple[0]][int(tuple[1]) - 1] == '*':
        #         return True

    def make_field(self):
        abc = "abcdefghij"
        field = [abc[i] + " " * 10 + "\n" for i in range(10)]
        return field

    def shoot_at(self, tuple):
        for ship in self.__ships:
            if tuple in ship:
                ship.shoot_at(tuple)

    def field_with_ship(self):
        i = 0
        for ship in self.__ships:
            if True in ship.get_hit():
                for damage in ship.get_hit():
                    if damage:
                        tuple = ship.coordinate[0][i]
                        self.draw(self.field_with, tuple, 'X')
            else:
                for cordinate in ship.coordinate[0]:
                    tuple = cordinate[i]
                    self.draw(self.field_with, tuple, '*')
            i += 1

    def get_ships(self):
        return self.__ships
