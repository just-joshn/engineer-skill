import unittest

from slug import slug


class SlugTests(unittest.TestCase):
    def test_normal_title(self):
        self.assertEqual(slug("Hello World"), "hello-world")

    def test_repeated_whitespace(self):
        self.assertEqual(slug("  Hello  \t World\n"), "hello-world")

    def test_empty_title(self):
        self.assertEqual(slug(" \t\n"), "")


if __name__ == "__main__":
    unittest.main()
