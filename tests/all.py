#!/usr/bin/env python3
import unittest
from src.lib import words_by_frequency

class TestStringMethods(unittest.TestCase):
    def statement(self):
        self.assertEqual(
            words_by_frequency("bar baz foo foo zblah zblah zblah baz toto bar", 3),
            [
                ("zblah", 3),
                ("bar", 2),
                ("baz", 2),
            ]
        )

    def special_characters(self):
        self.assertEqual(
            words_by_frequency("The quick, very quick brown fox jumps, jumps and jumps over the lazy dog dog dog dog! dogdogdog", 5),
            # 'dog!' is counted as a word, and so to 'jumps,'
            [('dog', 3), ('jumps', 2), ('the', 2), ('and', 1), ('brown', 1)]
        )

    def empty_sentence(self):
        self.assertEqual(words_by_frequency("", 20), [])

if __name__ == '__main__':
    unittest.main()