from user.Subreddit import Subreddit

__author__ = 'dylan'


class SubredditList:
    def __init__(self):
        self.subreddit_list = {}
        self.subreddit_count = 0
        self.comment_count = 0
        self.highest_comment = 0
        self.lowest_comment = 0
        self.total_ups = 0
        self.total_downs = 0

    def add_comment_list(self, subreddit):
        self.subreddit_list[subreddit.name] = subreddit
        self.subreddit_count += 1

    def add_comment(self, comment):
        if comment.ups > self.highest_comment:
            self.highest_comment = comment.ups
        if comment.downs > self.lowest_comment:
            self.lowest_comment = comment.downs

        if comment.subreddit in self.subreddit_list:
            self.subreddit_list[comment.subreddit].add_comment(comment)
        else:
            new_sub = Subreddit(comment.subreddit)
            new_sub.add_comment(comment)
            self.add_comment_list(new_sub)

    def get_total_comments(self):
        for subreddit in self.subreddit_list.values():
            self.comment_count += subreddit.comment_count
        return self.comment_count

    def get_subreddit_name_list(self):
        return self.subreddit_list.keys()

    def apply_total_comments(self, total_comments):
        for subreddit in self.subreddit_list.values():
            subreddit.set_total(total_comments)

    def get_percentage_breakdown(self):
        for subreddit in self.subreddit_list.values():
            print(str(subreddit.comment_count) + " " + str(subreddit.percentage) + "%")

    def total_ups_and_downs(self):
        for subreddit in self.subreddit_list.values():
            self.total_ups += subreddit.total_ups
            self.total_downs += subreddit.total_downs