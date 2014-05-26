__author__ = 'dylan'
import unittest
import json
import user.Subreddit


class TestSubreddit(unittest.TestCase):
    def setUp(self):
        with open("test.json") as json_file:
            self.test_json = json.load(json_file)


