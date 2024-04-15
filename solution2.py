class NavalBattle:
    playing_field = [[0] * 10 for _ in range(10)]
    field = [['~'] * 10 for _ in range(10)]

    def __init__(self, sign):
        self.hit = sign

    def shot(self, x, y):
        if NavalBattle.playing_field[y-1][x-1] == 1:
            NavalBattle.field[y-1][x-1] = self.hit
            print('попал')
        else:
            NavalBattle.field[y-1][x-1] = 'o'
            print('мимо')

    @staticmethod
    def show():
        for i in range(len(NavalBattle.field)):
            print(*NavalBattle.field[i])
