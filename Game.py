import Field as F
import Player as P


class Game:
    def __init__(self):
        self.__fields = []
        self.__players = []
        self.__current_player = 0

    def __init__(self):
        player_1 = P.Player("Anton")
        field_1 = F.Field()
        player_2 = P.Player("Max")
        field_2 = F.Field()

        self.__players.append(player_1)
        self.__players.append(player_2)
        self.__fields.append(field_1)
        self.__fields.append(field_2)

        self.__current_player = 0

    def read_position(self):
        return self.__players[self.__current_player].read_position()

    def field_without_ships(self, index):
        pass

    def field_with_ships(self):
        pass

    def have_winner(self):
        end = True
        for fields in self.__fields:
            for ship in fields.get_ships():
                if False in ship.get_hit():
                    end = False
        return end

    def start(self):
        i = 1
        while not self.have_winner():
            turn = self.read_position()
            while self.__fields[self.__current_player].has_ship(turn):
                # Перевіряєє чи людина попала
                self.__fields[self.__current_player].shoot_at(turn)
                print("Влучив")
                print(self.__fields[self.__current_player].shoot_at(turn).field_without_ship)
            self.__current_player = i % 2
            i += 1

game1 = Game()
# """
# Cстворюєму обєкт гри
# """
game1.start()
# """
# Запускаємо гру
# """

