import random as rd

from Ship import Ship, ABC

MAX_4CAMERS_SHIP = 1
MAX_3CAMERS_SHIP = 2
MAX_2CAMERS_SHIP = 3
MAX_1CAMERS_SHIP = 4

LEN_4CAMERS_SHIP = [(1, 4), (4, 1)]
LEN_3CAMERS_SHIP = [(1, 3), (3, 1)]
LEN_2CAMERS_SHIP = [(1, 2), (2, 1)]
LEN_1CAMERS_SHIP = (1, 1)

ALL_COORDINATES = [('a', 0), ('a', 1), ('a', 2), ('a', 3), ('a', 4), ('a', 5), ('a', 6), ('a', 7), ('a', 8), ('a', 9),
                   ('b', 0), ('b', 1), ('b', 2), ('b', 3), ('b', 4), ('b', 5), ('b', 6), ('b', 7), ('b', 8), ('b', 9),
                   ('c', 0), ('c', 1), ('c', 2), ('c', 3), ('c', 4), ('c', 5), ('c', 6), ('c', 7), ('c', 8), ('c', 9),
                   ('d', 0), ('d', 1), ('d', 2), ('d', 3), ('d', 4), ('d', 5), ('d', 6), ('d', 7), ('d', 8), ('d', 9),
                   ('e', 0), ('e', 1), ('e', 2), ('e', 3), ('e', 4), ('e', 5), ('e', 6), ('e', 7), ('e', 8), ('e', 9),
                   ('f', 0), ('f', 1), ('f', 2), ('f', 3), ('f', 4), ('f', 5), ('f', 6), ('f', 7), ('f', 8), ('f', 9),
                   ('g', 0), ('g', 1), ('g', 2), ('g', 3), ('g', 4), ('g', 5), ('g', 6), ('g', 7), ('g', 8), ('g', 9),
                   ('h', 0), ('h', 1), ('h', 2), ('h', 3), ('h', 4), ('h', 5), ('h', 6), ('h', 7), ('h', 8), ('h', 9),
                   ('i', 0), ('i', 1), ('i', 2), ('i', 3), ('i', 4), ('i', 5), ('i', 6), ('i', 7), ('i', 8), ('i', 9),
                   ('j', 0), ('j', 1), ('j', 2), ('j', 3), ('j', 4), ('j', 5), ('j', 6), ('j', 7), ('j', 8), ('j', 9)]



class Field:

    def __init__(self):
        self.__ships = []
        self.generate_field()
        self.field_without_ships = self.make_field()
        self.field_with_ships = self.make_field()

    def get_ships_coordinate(self):
        for ship in self.__ships:
            print(ship.coordinate)

    def get_field_without_ship(self):
        self.field_without_ships = self.make_field()

        for ship in self.__ships:
            if True in ship.get_hit():
                for i, damage in enumerate(ship.get_hit()):
                    if damage:
                        tuple = ship.coordinate[i]
                        self.draw(self.field_without_ships, tuple, 'X')
        return self.field_without_ships

    def draw(self, field, tuple, char):
        for index, row in enumerate(field[1:]):
            if int(row[0]) == tuple[1]:
                field[index + 1] = row[:ABC.index(tuple[0]) + 1] + char + row[ABC.index(tuple[0]) + 1:]
        return field



    def generate_xcamers_ship(self, x_camers):
        for i in range(x_camers.get("max")):
            ship = None
            while not ship:
                _ship = Ship(rd.choice(x_camers.get("len")))
                ship = None if self.has_ship(_ship) else _ship

            self.__ships.append(ship)

    def generate_field(self):
        self.generate_xcamers_ship({"max": MAX_4CAMERS_SHIP,
                                     "len": LEN_4CAMERS_SHIP})
                                                   
        self.generate_xcamers_ship({"max": MAX_3CAMERS_SHIP,
                                    "len": LEN_3CAMERS_SHIP})
                                                   
        self.generate_xcamers_ship({"max": MAX_2CAMERS_SHIP,
                                    "len": LEN_2CAMERS_SHIP})
                                                   
        self.generate_1camers_ship()

    def generate_1camers_ship(self):

        for i in range(MAX_1CAMERS_SHIP):
            ship_coordinate = rd.choice(list(self.get_not_used_coordinates()))
            ship_coordinate = (ABC.index(ship_coordinate[0]), ship_coordinate[1])
            self.__ships.append(Ship(LEN_1CAMERS_SHIP, ship_coordinate))

    def get_not_used_coordinates(self):
        already_used_coordinates = set()
        for _ship in self.__ships:
            already_used_coordinates.update(_ship.coordinate + _ship.empty_ships_fields)
        return set(ALL_COORDINATES).symmetric_difference(already_used_coordinates)

    def has_ship(self, check_ship):

        ship_exists = False
        check_ship_coordinates = set(check_ship.coordinate + check_ship.empty_ships_fields)

        for _ship in self.__ships:
            _ship_coordinates = set(_ship.coordinate)

            if check_ship_coordinates.intersection(_ship_coordinates):
                ship_exists = True
                break

        return ship_exists

    def make_field(self):
        abc = "abcdefghij"
        field = [' ' + abc]
        for i in range(10):
            field.append(str(i) + " " * 10)
        return field

    def shoot_at(self, tuple):
        shoot = False
        for ship in self.__ships:
            if tuple in ship.coordinate:
                ship.shoot_at(tuple)
                shoot = True
                break
        return shoot

    def get_field_with_ship(self):
        self.field_with_ship = self.make_field()

        for ship in self.__ships:
            if True in ship.get_hit():
                for i, damage in enumerate(ship.get_hit()):
                    if damage:
                        tuple = ship.coordinate[i]
                        self.draw(self.field_with_ship, tuple, 'X')

        for ship in self.__ships:
            for coordinate in ship.coordinate:
                self.draw(self.field_with_ship, coordinate, '*')

        return self.field_with_ship

    def get_ships(self):
        return self.__ships



