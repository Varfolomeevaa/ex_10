class NavalBattle:
    '''
    class of game Naval Battle
    '''
    playing_field = [[0] * 10 for _ in range(10)]
    field = [['~'] * 10 for _ in range(10)]

    def __init__(self, sign):
        '''
        method for initialization
        :param sign: sign of player
        '''
        self.hit = sign

    def shot(self, x, y):
        '''
        method of shoting a point
        :param x: coordinate of line
        :param y: coordinate of column
        :return: None
        '''
        if NavalBattle.playing_field[y-1][x-1] == 1:
            NavalBattle.field[y-1][x-1] = self.hit
            print('попал')
        else:
            NavalBattle.field[y-1][x-1] = 'o'
            print('мимо')

    @staticmethod
    def show():
        '''
        method for showing playing field
        :return: None
        '''
        for i in range(len(NavalBattle.field)):
            print(*NavalBattle.field[i])
