from datetime import datetime

__author__ = 'dylan'


class Comment:
    def __init__(self, body, body_html, author, link_author, subreddit, link_title, edited, name, link_url, time, ups,
                 downs):
        self.body = body
        self.body_html = body_html
        self.author = author
        self.link_author = link_author
        self.subreddit = subreddit
        self.link_title = link_title
        self.link_url = link_url
        self.edited = edited
        self.name = name
        self.time = str(datetime.utcfromtimestamp(time))
        self.ups = ups
        self.downs = downs

    def __str__(self):
        return self.link_title + "\nSubreddit:" + self.subreddit + "\n" + self.body

    def __repr__(self):
        return "Title: " + self.link_title + " Subreddit: " + self.subreddit + " Body:" + self.body + "\n"
