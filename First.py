import random as rd


class Field:
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

    def is_valid(self, data):
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
            c.append(count[0])
            for i in range(2, 5):
                c.append(int(count[i]/i))
            if c == [4, 3, 2, 1]:
                return True
            else:
                return False
        else:
            return False

    def field_to_str(self, data):
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
                ship = self.generate_ship([1, 12 - len], len)
                print(ship)
                build = True

                area = self.no_ship(ship, len)
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

    def generate_ship(self, limits, len):
        coordinate = []
        abc = "abcdefghij"

        way = int(rd.uniform(0, 2))
        head_x = int(rd.uniform(limits[0], limits[1]))
        head_y = int(rd.uniform(limits[0], limits[1]))

        if way == 0:
            for i in range(len):
                coordinate.append((abc[head_y], head_x + i))
        else:
            for i in range(len - 1):
                coordinate.append((abc[head_y + i], head_x))
        return coordinate

    def x_area(self, abc, coordinate):
        area = []
        if coordinate[0][0] in abc[1:-1] and coordinate[-1][0] in abc[1:-1]:
            if coordinate[0][1] > 1 and coordinate[-1][1] < 10:
                lit = abc.index(coordinate[0][0]) - 1
                start = coordinate[0][1] - 1
                end = coordinate[-1][1] + 1

                for j in range(1, 4):
                    c = [(abc[lit], i) for i in range(start, end + 1)]
                    lit += 1
                    area.append(c)
            else:
                lit = abc.index(coordinate[0][0]) - 1
                if coordinate[0][1] == 1:
                    start = coordinate[0][1]
                    end = coordinate[-1][1] + 1
                else:
                    start = coordinate[0][1] - 1
                    end = coordinate[-1][1]

                for j in range(1, 4):
                    c = [(abc[lit], i) for i in range(start, end + 1)]
                    lit += 1
                    area.append(c)
        else:
            if coordinate[0][0] == 'a':
                lit = abc.index(coordinate[0][0])
                if coordinate[0][1] > 1 and coordinate[-1][1] < 10:
                    start = coordinate[0][1] - 1
                    end = coordinate[-1][1] + 1
                elif coordinate[0][1] == 1:
                    start = coordinate[0][1]
                    end = coordinate[-1][1] + 1
                elif coordinate[-1][1] == 10:
                    start = coordinate[0][1] + 1
                    end = coordinate[-1][1]

                for j in range(1, 3):
                    c = [(abc[lit], i) for i in range(start, end + 1)]
                    lit += 1
                    area.append(c)
            else:
                lit = abc.index(coordinate[0][0]) - 1
                if coordinate[0][1] > 1 and coordinate[-1][1] < 10:
                    start = coordinate[0][1] - 1
                    end = coordinate[-1][1] + 1
                elif coordinate[0][1] == 1:
                    start = coordinate[0][1]
                    end = coordinate[-1][1] + 1
                elif coordinate[-1][1] == 10:
                    start = coordinate[0][1] + 1
                    end = coordinate[-1][1]

                for j in range(1, 3):
                    c = [(abc[lit], i) for i in range(start, end + 1)]
                    lit += 1
                    area.append(c)
        return area

    def no_ship(self, coordinate, len):
        abc = "abcdefghij"
        area = []

        if coordinate[0][1] == coordinate[-1][1]:
            area = self.x_area(abc, coordinate)
        else:
            if coordinate[0][0] in abc[1:-len]:
                if coordinate[0][1] > 1 and coordinate[-1][1] < 10:
                    start = abc.index(coordinate[0][0]) - 1
                    end = abc.index(coordinate[-1][0]) + 2
                    number = coordinate[0][1] - 1

                    for i in range(3):
                        l = [(letter, number) for letter in abc[start: end]]
                        number += 1
                        area.append(l)
                else:
                    start = abc.index(coordinate[0][0]) - 1
                    end = abc.index(coordinate[-1][0]) + 1
                    number = coordinate[0][1]

                    for i in range(2):
                        l = [(letter, number) for letter in abc[start: end]]
                        if coordinate[0][1] == 1:
                            number += 1
                        else:
                            number -= 1
                        area.append(l)
            else:
                if coordinate[0][1] > 1 and coordinate[-1][1] < 10:
                    start = abc.index(coordinate[0][0]) - 1
                    end = abc.index(coordinate[-1][0])
                    number = coordinate[0][1] - 1

                    for i in range(3):
                        l = [(letter, number) for letter in abc[start: end]]
                        number += 1
                        area.append(l)
                else:
                    number = coordinate[0][1]
                    if coordinate[0][1] == 1:
                        start = abc.index(coordinate[0][0])
                        end = abc.index(coordinate[-1][0]) + 2
                    else:
                        start = abc.index(coordinate[0][0])
                        end = abc.index(coordinate[-1][0]) + 2
                        number = coordinate[0][1]

                    for i in range(2):
                        l = [(letter, number) for letter in abc[start:end]]
                        if coordinate[0][1] == 1:
                            number += 1
                        else:
                            number -= 1
                        area.append(l)
        return area
field = Field()
# print(field.read_field("T.txt"))
data = field.read_field("T.txt")
field.__setattr__("data", data)
# print(field.is_valid(data))
# print(field.field_to_str(data))
print(field.generate_field())

