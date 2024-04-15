import random


class NavalBattle:
    playing_field = []
    field = [['~'] * 10 for _ in range(10)]

    def __init__(self, sign):
        self.hit = sign

    def shot(self, x, y):
        if not NavalBattle.playing_field:
            print('игровое поле не заполнено')
        else:
            if NavalBattle.field[y - 1][x - 1] == '~':
                if NavalBattle.playing_field[y - 1][x - 1] == 1:
                    NavalBattle.field[y - 1][x - 1] = self.hit
                    print('попал')
                else:
                    NavalBattle.field[y - 1][x - 1] = 'o'
                    print('мимо')
            else:
                print('ошибка')

    @staticmethod
    def show():
        for i in range(len(NavalBattle.field)):
            print(*NavalBattle.field[i])

    @classmethod
    def new_game(cls):
        cls.playing_field = [[-1] * 10 for _ in range(10)]
        count_ships_need = [4, 3, 2, 1]
        count_ships = [0, 0, 0, 0]
        for i in range(4, 0, -1):
            while count_ships[i - 1] != count_ships_need[i - 1]:
                rand_i = random.randint(0, 9)
                rand_j = random.randint(0, 9)
                flag_1 = False
                if rand_j + i <= 9 or rand_j - i >= 0 or rand_i + i <= 9 or rand_i - i >= 0:
                    if rand_j + i <= 9:
                        if cls.playing_field[rand_i][rand_j:rand_j + i] == [-1] * i:
                            if (rand_j - 1 >= 0 and rand_j + 1 <= 9 and cls.playing_field[rand_i][rand_j - 1] != 1 and
                                cls.playing_field[rand_i][
                                    rand_j + i] != 1) or (
                                    rand_j + 1 <= 9 and cls.playing_field[rand_i][rand_j + i] != 1) or (
                                    rand_j - 1 >= 0 and cls.playing_field[rand_i][rand_j - 1] != 1 and
                                    cls.playing_field[rand_i]):
                                if rand_i == 0:
                                    flag_1 = cls.playing_field[rand_i + 1][rand_j:rand_j + i] != [1] * i
                                elif rand_i == 9:
                                    flag_1 = cls.playing_field[rand_i - 1][rand_j:rand_j + i] != [1] * i
                                else:
                                    flag_1 = cls.playing_field[rand_i + 1][rand_j:rand_j + i] != [1] * i and \
                                             cls.playing_field[rand_i - 1][rand_j:rand_j + i] != [1] * i
                            else:
                                flag_1 = False
                            if flag_1:
                                cls.playing_field[rand_i][rand_j:rand_j + i] = [1] * i
                                count_ships[i - 1] += 1
                                if rand_i == 0:
                                    cls.playing_field[rand_i + 1][rand_j:rand_j + i] = [0] * i
                                elif rand_i == 9:
                                    cls.playing_field[rand_i - 1][rand_j:rand_j + i] = [0] * i
                                else:
                                    cls.playing_field[rand_i + 1][rand_j:rand_j + i] = [0] * i
                                    cls.playing_field[rand_i - 1][rand_j:rand_j + i] = [0] * i
                    if rand_j - i >= 0 and not flag_1:
                        if cls.playing_field[rand_i][rand_j - i + 1:rand_j + 1] == [-1] * i:
                            if (rand_j + 1 <= 9 and rand_j - i >= 0 and cls.playing_field[rand_i][rand_j - i] != 1 and
                                cls.playing_field[rand_i][
                                    rand_j + 1] != 1) or (
                                    rand_j - i >= 0 and cls.playing_field[rand_i][rand_j - i] != 1) or (
                                    rand_j + 1 <= 9 and cls.playing_field[rand_i][
                                rand_j + 1] != 1):
                                if rand_i == 0:
                                    flag_1 = cls.playing_field[rand_i + 1][rand_j - i + 1:rand_j + 1] != [1] * i
                                elif rand_i == 9:
                                    flag_1 = cls.playing_field[rand_i - 1][rand_j - i + 1:rand_j + 1] != [1] * i
                                else:
                                    flag_1 = cls.playing_field[rand_i + 1][rand_j - i + 1:rand_j + 1] != [1] * i and \
                                             cls.playing_field[rand_i - 1][rand_j - i + 1:rand_j + 1] != [1] * i
                            else:
                                flag_1 = False
                            if flag_1:
                                cls.playing_field[rand_i][rand_j - i + 1:rand_j + 1] = [1] * i
                                count_ships[i - 1] += 1
                                if rand_i == 0:
                                    cls.playing_field[rand_i + 1][rand_j - i + 1:rand_j + 1] = [0] * i
                                elif rand_i == 9:
                                    cls.playing_field[rand_i - 1][rand_j - i + 1:rand_j + 1] = [0] * i
                                else:
                                    cls.playing_field[rand_i + 1][rand_j - i + 1:rand_j + 1] = [0] * i
                                    cls.playing_field[rand_i - 1][rand_j - i + 1:rand_j + 1] = [0] * i

                    if rand_i + i <= 9 and not flag_1:
                        if (rand_i - 1 >= 0 and rand_i + i + 1 <= 9 and cls.playing_field[rand_i - 1][rand_j] != 1 and
                            cls.playing_field[rand_i + i + 1][
                                rand_j] != 1) or (rand_i - 1 >= 0 and cls.playing_field[rand_i - 1][rand_j] != 1) or (
                                rand_i + i + 1 <= 9 and cls.playing_field[rand_i + i + 1][
                            rand_j] != 1):
                            flag_2 = True
                            for j in range(i):
                                if cls.playing_field[rand_i + j][rand_j] != -1:
                                    flag_2 = False
                                if rand_j - 1 >= 0:
                                    if cls.playing_field[rand_i + j][rand_j - 1] == 1:
                                        flag_2 = False
                                else:
                                    if cls.playing_field[rand_i + j][rand_j + 1] == 1:
                                        flag_2 = False
                                if rand_j + 1 <= 9:
                                    if cls.playing_field[rand_i + j][rand_j + 1] == 1:
                                        flag_2 = False
                                else:
                                    if cls.playing_field[rand_i + j][rand_j - 1] == 1:
                                        flag_2 = False
                            if flag_2:
                                flag_1 = True
                                count_ships[i - 1] += 1
                                for j in range(i):
                                    cls.playing_field[rand_i + j][rand_j] = 1
                                    if rand_j - 1 >= 0:
                                        cls.playing_field[rand_i + j][rand_j - 1] = 0
                                    else:
                                        cls.playing_field[rand_i + j][rand_j + 1] = 0
                                    if rand_j + 1 <= 9:
                                        cls.playing_field[rand_i + j][rand_j + 1] = 0
                                    else:
                                        cls.playing_field[rand_i + j][rand_j - 1] = 0
                    if rand_i - i >= 0 and not flag_1:
                        if (rand_i + 1 <= 9 and rand_i - i >= 0 and cls.playing_field[rand_i + 1][rand_j] != 1 and
                            cls.playing_field[rand_i - i][rand_j] != 1) or (
                                rand_i + 1 <= 9 and cls.playing_field[rand_i + 1][rand_j] != 1) or (
                                rand_i - i >= 0 and cls.playing_field[rand_i - i][rand_j] != 1):
                            flag_2 = True
                            for j in range(i):
                                if cls.playing_field[rand_i - j][rand_j] != -1:
                                    flag_2 = False
                                if rand_j - 1 >= 0:
                                    if cls.playing_field[rand_i - j][rand_j - 1] == 1:
                                        flag_2 = False
                                else:
                                    if cls.playing_field[rand_i - j][rand_j + 1] == 1:
                                        flag_2 = False
                                if rand_j + 1 <= 9:
                                    if cls.playing_field[rand_i - j][rand_j + 1] == 1:
                                        flag_2 = False
                                else:
                                    if cls.playing_field[rand_i - j][rand_j - 1] == 1:
                                        flag_2 = False
                            if flag_2:
                                flag_1 = True
                                count_ships[i - 1] += 1
                                for j in range(i):
                                    cls.playing_field[rand_i - j][rand_j] = 1
                                    if rand_j - 1 >= 0:
                                        cls.playing_field[rand_i - j][rand_j - 1] = 0
                                    else:
                                        cls.playing_field[rand_i - j][rand_j + 1] = 0
                                    if rand_j + 1 <= 9:
                                        cls.playing_field[rand_i - j][rand_j + 1] = 0
                                    else:
                                        cls.playing_field[rand_i - j][rand_j - 1] = 0

        for i in range(10):
            for j in range(10):
                if cls.playing_field[i][j] == -1:
                    cls.playing_field[i][j] = 0
        NavalBattle.field = [['~'] * 10 for _ in range(10)]
