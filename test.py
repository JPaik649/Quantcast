from argparse import Namespace
import unittest
import most_active_cookie as cookie
from unittest.mock import patch
import io

class CookieTestMethods(unittest.TestCase):

    def setUp(self):
        self.cookieMap = {'2018': {'12': {'09': [('AtY0laUfhglK3lC7', 2), ('SAZuXPGUrfbcn5UA', 1), ('5UAVanZf6UtGyKVS', 1)], '08': [('SAZuXPGUrfbcn5UA', 1), ('4sMM2LxV07bPJzwf', 1), ('fbcn5UAVanZf6UtG', 1)], '07': [('4sMM2LxV07bPJzwf', 1)]}}}

    def test_integration1(self):
        with patch('sys.stdout', new = io.StringIO()) as fake_out:
            args = Namespace(filename = "test.csv", date="2018-12-09")
            cookie.cookie(args)
            self.assertEqual(fake_out.getvalue().strip(), "AtY0laUfhglK3lC7")

    def test_integration2(self):
        with patch('sys.stdout', new = io.StringIO()) as fake_out:
            args = Namespace(filename = "test.csv", date="2018-12-24")
            cookie.cookie(args)
            self.assertEqual(fake_out.getvalue().strip(), "No cookies active on this day")

    def test_fileParsing(self):
        self.assertEqual(cookie.parsefile("test.csv"), self.cookieMap)
    
    def test_findCookie1(self):
        date = ["2018", "12", "09"]
        self.assertEqual(cookie.findCookie(self.cookieMap, date), ["AtY0laUfhglK3lC7"])

    def test_findCookie2(self):
        date = ["2018", "12", "08"]
        self.assertEqual(cookie.findCookie(self.cookieMap, date), ["SAZuXPGUrfbcn5UA", "4sMM2LxV07bPJzwf", "fbcn5UAVanZf6UtG"])

    def test_findCookie3(self):
        date = ["2018", "12", "03"]
        self.assertEqual(cookie.findCookie(self.cookieMap, date), None)

if __name__ == "__main__":
    unittest.main()