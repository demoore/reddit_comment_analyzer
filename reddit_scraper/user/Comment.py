from datetime import datetime

__author__ = 'dylan'


class Comment:
    def __init__(self, body, body_html, author, link_author, subreddit, link_title, edited, name, link_url, time, ups,
                 downs, comment_id, link_id):
        self.body = body
        self.body_html = body_html
        self.author = author
        self.link_author = link_author
        self.subreddit = subreddit
        self.link_title = link_title
        self.context_link = link_title.replace(' ', '_').replace('\'', '')
        self.link_url = link_url
        self.edited = edited
        self.name = name
        self.time = str(datetime.utcfromtimestamp(time))
        self.ups = ups
        self.downs = downs
        self.comment_id = comment_id
        self.link_id = link_id
        self.context_url = (
            "http://www.reddit.com/r/{}/comments/{}/{}/{}" .format( subreddit, link_id.split('_')[-1], self.context_link,
            comment_id))

    def __str__(self):
        return self.link_title + "\nSubreddit:" + self.subreddit + "\n" + self.body

    def __repr__(self):
        return "Title: " + self.link_title + " Subreddit: " + self.subreddit + " Body:" + self.body + "\n"
