#!/usr/bin/env python3
import unittest
from src.lib import words_by_frequency

class TestWordsByFrequency(unittest.TestCase):
    def test_statement(self):
        self.assertEqual(
            words_by_frequency("bar baz foo foo zblah zblah zblah baz toto bar", 3),
            [
                ("zblah", 3),
                ("bar", 2),
                ("baz", 2),
            ]
        )

    def test_special_characters(self):
        self.assertEqual(
            words_by_frequency("The quick, very quick brown fox jumps, jumps and jumps over the lazy dog dog dog dog! dogdogdog", 5),
            # 'dog!' is counted as a word, and so to 'jumps,'
            [('dog', 3), ('jumps', 2), ('the', 2), ('and', 1), ('brown', 1)]
        )

    def test_empty_sentence(self):
        self.assertEqual(words_by_frequency("", 20), [])

    def test_invalid(self):
        self.assertEqual(words_by_frequency("bar baz foo foo zblah zblah zblah baz toto bar", -1), [])
        self.assertEqual(words_by_frequency("bar baz foo foo zblah zblah zblah baz toto bar", 0), [])

if __name__ == '__main__':
    unittest.main()