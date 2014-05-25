from collections import Counter, defaultdict
import json

from urllib import request, error
from time import sleep
import jinja2
from user.Comment import *
from user.SubredditList import SubredditList


__author__ = 'dylan'


def get_comments(url, delay=2):
    sleep(delay)
    try:
        opener = request.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        req = opener.open(url)
        data = req.read().decode('utf8')
        comments = json.loads(data)
        return comments
    except error.HTTPError as e:
        if e.code == 429:
            print("Code 429, too many requests!")
            sleep(delay + 7)
            opener = request.build_opener()
            opener.addheaders = [('User-agent', 'Mozilla/5.0')]
            req = opener.open(url)
            data = req.read().decode('utf8')
            comments = json.loads(data)
            return comments


def scrape_user(user_name, limit=100, next_page=""):
    if next_page != "":
        user_url = "http://www.reddit.com/user/" + user_name + "/comments.json?limit=" + str(
            limit) + "&after=" + next_page
    else:
        user_url = "http://www.reddit.com/user/" + user_name + "/comments.json?limit=" + str(limit)

    user_comments = get_comments(user_url, delay=2)

    print(user_url)

    comment_list = list()
    subreddit_next = list()
    new_list = list()

    for entry in user_comments['data']['children']:
        comment = Comment(str(entry['data']['body']),
                          jinja2.Markup(str(entry['data']['body_html'])).unescape(),
                          str(entry['data']['author']),
                          str(entry['data']['link_author']),
                          str(entry['data']['subreddit']),
                          str(entry['data']['link_title']),
                          str(entry['data']['edited']),
                          str(entry['data']['name']),
                          str(entry['data']['link_url']),
                          entry['data']['created_utc'],
                          entry['data']['ups'],
                          entry['data']['downs'])
        comment_list.append(comment)

        subreddit_next.append(str(entry['data']['name']))

    if len(subreddit_next) != 0:
        next_page = subreddit_next[-1]
        new_list = scrape_user(user_name, limit, next_page)

    comment_list.extend(new_list)
    return comment_list


def get_comment_count(comment_list):
    subreddit_count = Counter(subreddit for subreddit in comment_list)
    return subreddit_count

def make_subreddit_list(comment_list):
    subreddit_list = SubredditList()
    for comment in comment_list:
        subreddit_list.add_comment(comment)
    return subreddit_list

