__author__ = 'dylan'
import unittest
import scraper


class DryRun(unittest.TestCase):
    def setUp(self):
        self.comment_list = ()
        self.sub_list = ()

    def test_scraper(self):
        self.comment_list = scraper.scrape_user("zardoz90", 100, "")
        self.assertTrue(True, "We made it this far")


if __name__ == '__main__':
    unittest.main()