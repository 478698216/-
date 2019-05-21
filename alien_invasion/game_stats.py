import os

class GameStats():
    '''跟踪游戏的统计信息'''

    def __init__(self, ai_settings):
        '''初始化统计信息'''
        self.ai_settings = ai_settings
        self.reset_stats()

        # 游戏刚启动时处于非活动状态
        self.game_active = False

        # 在任何情况下都不应该重置最高得分
        if os.path.exists('highscore.txt'):
            self.open_highscore()
        else:
            self.high_score = 0

    def reset_stats(self):
        '''初始化在游戏运行期间可能变化的统计信息'''
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def open_highscore(self):
        '''读取最高得分'''
        filename = 'highscore.txt'

        with open(filename) as file_object:
            self.high_score = int(file_object.read())