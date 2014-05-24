__author__ = 'dylan'


class User(object):
    def __init__(self, name, user_info=list()):
        self.name = name
        self.user_info = user_info

    @property
    def user_info(self):
        return self.user_info
    @user_info.setter
    def user_info(self, value):
        self.user_info = value
