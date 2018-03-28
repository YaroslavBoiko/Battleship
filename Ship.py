import random as rd

LIMITS = {
    'left': 0,
    'right': 10
}
ABC = "abcdefghij"


class Ship:
    def __init__(self, length, head=None, empty_ships_fields_flag=True):
        self.__length = length
        self.coordinate, self.horizontal = self.generate_ship(length, head)
        self.__hit = [False] * length[0] if length[0] > 1 else [False] * length[1]
        self.bow = self.coordinate[0]
        self.empty_ships_fields = self.get_ship_empty_fields() if empty_ships_fields_flag else None

    def shoot_at(self, shoot_coordinate):
        try:
            self.__hit[self.coordinate.index(shoot_coordinate)] = True
            return True
        except ValueError:
            return False

    def get_length(self):
        return self.__length

    def get_hit(self):
        return self.__hit
    
    def generate_ship(self, length, head):
        
        x_length, y_length = length

        if head:
            head_x = head[0]
            head_y = head[1]
        else:
            head_x = int(rd.uniform(LIMITS.get('left'), LIMITS.get('right') - x_length))
            head_y = int(rd.uniform(LIMITS.get('left'), LIMITS.get('right') - y_length))

        
        if x_length > 1:
            return self.horizontal_ship(head_x, head_y, x_length)
        else:
            return self.vertical_ship(head_x, head_y, y_length)
            

    def horizontal_ship(self, head_x, head_y, length):
        return ([(ABC[head_x + i], head_y) for i in range(length)], True)

    def vertical_ship(self, head_x, head_y, length):
        return ([(ABC[head_x], head_y + i) for i in range(length)], False)

    def get_ship_empty_fields(self):
        """
                                    up_ship

        left_up_coordinate     -->e |e e e| e      <--rigth_up_coordinate
        left_ship              -->e |x x x| e      <-- rigth_ship
        left_down_coordinate   -->e |e e e| e      <-- rigth_down_coordinate

                                    down_ship

        """
        empty_fields_coordinate = []

        head_x = ABC.index(self.bow[0])
        head_y = self.bow[1]

        if head_x - 1 > 0:
            left_ship = Ship((1, self.get_length()[1]), (head_x - 1, head_y), empty_ships_fields_flag=False)
            empty_fields_coordinate += left_ship.coordinate

            if head_y - 1 > 0:
                left_up_coordinate = (ABC[head_x - 1], head_y - 1)
                empty_fields_coordinate.append(left_up_coordinate)

        if head_x + self.get_length()[0] < 10:
            rigth_ship = Ship((1, self.get_length()[1]), (head_x + self.get_length()[0], head_y),
                              empty_ships_fields_flag=False)
            empty_fields_coordinate += rigth_ship.coordinate

            if head_y - 1 > 0:
                rigth_up_coordinate = (ABC[head_x + self.get_length()[0]], head_y - 1)
                empty_fields_coordinate.append(rigth_up_coordinate)

        if head_y - 1 > 0:
            up_ship = Ship((self.get_length()[0], 1), (head_x, head_y - 1), empty_ships_fields_flag=False)
            empty_fields_coordinate += up_ship.coordinate

        if head_y + self.get_length()[1] < 10:
            down_ship = Ship((self.get_length()[0], 1), (head_x, head_y + self.get_length()[1]),
                             empty_ships_fields_flag=False)
            empty_fields_coordinate += down_ship.coordinate

            if head_x + self.get_length()[0] < 10:
                rigth_down_coordinate = (ABC[head_x + self.get_length()[0]], head_y + self.get_length()[1])
                empty_fields_coordinate.append(rigth_down_coordinate)

            if head_x - 1 > 0:
                left_down_coordinate = (ABC[head_x - 1], head_y + self.get_length()[1])
                empty_fields_coordinate.append(left_down_coordinate)

        return empty_fields_coordinate

