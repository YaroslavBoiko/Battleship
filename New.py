import random as rd

class Field:
    def ship_size(self, coordinate):
        return True

    def read_field(self, file_name):
        with open(file_name, "r") as f:
            field = f.read().split("\n")
            abc = "abcdefghij"
            dict = {}

            for row in range(len(field)):
                dict[abc[row]] = field[row]
            # data = []
            # count = []

            # for row in range(len(field)):
            #     for c in range(len(row)):
            #         if field[row][c] == '*':
            #             len = self.ship_size(field[row][c])
            #             count[len - 1] += 1
            return dict

    def has_ship(self, data, tuple):
        if "*"not in data[tuple[0]]:
            return False
        else:
            if data[tuple[0]][int(tuple[1]) - 1] == '*':
                return True

    def ship_size(self, data, tuple):
        key = list(data.keys())
        index = int(tuple[1] - 1)
        len = 1
        len_right = 1
        len_up = 0

        if data[tuple[0]][index] == " ":
            return 0
        else:
            try:
                if data[tuple[0]][index + 1] == '*':
                    while True:
                        if len + index == 10:
                            break
                        if data[tuple[0]][index + len] != '*':
                            break
                        else:
                            len += 1

                if data[tuple[0]][index - 1] == '*':
                    while True:
                        if index - len_right == 0:
                            break
                        if data[tuple[0]][index - len_right] == '*':
                            len_right += 1
                        else:
                            len_right -= 1
                            break
                    return len + len_right
            except IndexError:
                len = 1
                if data[tuple[0]][index - 1] == '*':
                    while True:
                        if data[tuple[0]][index - len] == '*':
                            len += 1
                        else:
                            return len
        if len <= 1 and len_right <= 1:
            id = key.index(tuple[0])
            len = 0
            if id < 9:
                if data[key[id + 1]][index] == '*':
                    while data[key[id + len]][index] == '*':
                        if id + len == 9:
                            break
                        len += 1
                if id > 1:
                    if data[key[id - 1]][index] == '*':
                        while data[key[id - len_up]][index] == '*':
                            if id - len_up == 0:
                                break
                            len_up += 1
                    if len != 0 and len_up != 0:
                        return len + len_up - 1
        return len + len_up

    def is_valid(self,data):
        count = [0] * 5
        c = []
        if len(data.keys()) == 10:
            for key in data.keys():
                i = 1
                if len(data[key]) == 10 or len(data[key]):
                    for char in data[key]:
                        if char == "*":
                            tup = (key, i)
                            l = self.ship_size(data, tup)
                            count[l] = count[l] + 1
                        i = i + 1
            #c = [count[len]/len for len in range(2, 5)]
            c.append(count[0])
            for i in range(2, 5):
                c.append(int(count[i]/i))
            if c == [4, 3, 2, 1]:
                return True
            else:
                return False
        else:
            return False
    def field_to_str(self,data):
        st = ""
        for key in data.keys():
            st += data[key] + "\n"
        return st

    def generate_field(self):
        boats = []
        for i in range(4):
            c = 0
            len = 4 - i
            count = 5 - len
            while True:
                ship = self.generate_ship([1, 12 -len], len)
                print(ship)
                build = True

                area = self.no_ship(ship)
                for row in area:
                    for el in row:
                        if self.has_ship(self.data, el):
                              build = False
                        if build:
                            boats.append(ship)
                            c += 1
                        if c == count:
                            break
        return boats
