from user.Subreddit import Subreddit

__author__ = 'dylan'
from user import Comment


class SubredditList:
    def __init__(self):
        self.subreddit_list = {}
        self.subreddit_count = 0

    def add_comment_list(self, subreddit):
        self.subreddit_list[subreddit.name]  = subreddit
        self.subreddit_count += 1

    def add_comment(self, comment):
        if comment.subreddit in self.subreddit_list:
            self.subreddit_list[comment.subreddit].add_comment(comment)
        else:
            new_sub = Subreddit(comment.subreddit)
            new_sub.add_comment(comment)
            self.subreddit_count += 1
            self.add_comment_list(new_sub)

    def get_total_comments(self):
        comment_count = 0
        for subreddit in self.subreddit_list:
            comment_count += subreddit.comment_count
        return comment_count

    def get_subreddit_name_list(self):
        return self.subreddit_list.keys()
