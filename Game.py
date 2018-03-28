from Field import Field
from Player import Player


class Game:
    def __init__(self):
        self.__players = [Player("Anton"), Player("Max")]
        self.__fields = [Field(), Field()]

        self.__current_player = 0
        self.__current_field = 1

    def get_filed(self, index):
        return self.__fields[index]

    def read_position(self):
        return self.__players[self.__current_player].read_position()

    def field_without_ships(self, index):
        return self.__fields[index].get_field_without_ship()

    def field_with_ships(self, index):
        field = self.__fields[index].get_field_with_ship()
        for row in field:
            yield row

    def have_winner(self):
        is_winner = False
        for fields in self.__fields:
            ships_count = 0
            for ship in fields.get_ships():
                if all(ship.get_hit()):
                    ships_count += 1
            if ships_count == 10:
                is_winner = True
        return is_winner

    def change_player(self):
        if self.__current_player == 0:
            self.__current_player = 1
            self.__current_field = 0
        else:
            self.__current_player = 0
            self.__current_field = 1

    def start(self):
        print("First field")
        for row in self.field_with_ships(0):
            print(row)
        print("Second field")
        for row in self.field_with_ships(1):
            print(row)

        while not self.have_winner():
            turn = self.read_position()
            shoot = self.__fields[self.__current_field].shoot_at(turn)
            while shoot:
                print("Hit")
                turn = self.read_position()
                shoot = self.__fields[self.__current_field].shoot_at(turn)
            print("Sorry, you didn't hit!")
            self.change_player()


if '__main__':

    game1 = Game()
    game1.start()

