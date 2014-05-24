import jinja2

__author__ = 'dylan'


class Comment:
    def __init__(self, body, body_html, author, link_author, subreddit, link_title, edited, name):
        self.body = body
        self.body_html = body_html
        self.author = author
        self.link_author = link_author
        self.subreddit = subreddit
        self.link_title = link_title
        self.edited = edited
        self.name = name

    def __str__(self):
        return self.link_title + "\nSubreddit:" + self.subreddit + "\n" + self.body

    def __repr__(self):
        return "Title: " + self.link_title + " Subreddit: " + self.subreddit + " Body:" + self.body + "\n"
