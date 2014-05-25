__author__ = 'dylan'


class Subreddit:
    def __init__(self, name):
        self.name = name
        self.total_comment_count = 0
        self.percentage = 0.0
        self.comment_list = list()
        self.comment_count = 0

    def __str__(self):
        return "Subreddit:" + self.name + " Comment Count:" + str(self.comment_count)

    def __eq__(self, other):
        return (self.name == other.name) == 0

    __repr__ = __str__

    def add_comment(self, comment):
        self.comment_list.append(comment)
        self.comment_count += 1

    def set_total(self, total_comments):
        self.total_comment_count = total_comments
        self.percentage = (self.comment_count / (total_comments + 0.0)) * 100
