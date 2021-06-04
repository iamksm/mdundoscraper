import unittest

from scraper import scraper


class TestScraper(unittest.TestCase):

    def test_find_songs(self):
        """
        Test that it actually get's results on inputing Correct Data
        """
        result = scraper.find_songs('Khaligraph')
        self.assertIsNotNone(result)

    def test_list_artists(self):
        """
        Test to make sure it actually get's results
        """
        result = scraper.list_artists('K')
        self.assertIsNotNone(result)

        result = scraper.list_artists(' k')
        self.assertIsNotNone(result)

        result = scraper.list_artists('#')
        self.assertIsNotNone(result)

        result = scraper.list_artists('$')
        self.assertIsNotNone(result)

        result = scraper.list_artists('=')
        self.assertEqual(result, [])
