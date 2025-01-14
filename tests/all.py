#!/usr/bin/env python3
import unittest
from src.lib import words_by_frequency

class TestStringMethods(unittest.TestCase):
    def test_statement(self):
        self.assertEqual(
            words_by_frequency("bar baz foo foo zblah zblah zblah baz toto bar", 3),
            [
                ("zblah", 3),
                ("bar", 2),
                ("baz", 2),
            ])

    # def test_brown_fox(self):
    #     print(word_frequency("The quick, very quick brown fox jumps, jumps and jumps over the lazy dog dog dog dog! dogdogdog"))
    #     self.assertEqual(
    #         word_frequency("The quick, very quick brown fox jumps, jumps and jumps over the lazy dog dog dog dog! dogdogdog"),
    #         {
    #             "the": 2,
    #             "quick": 2,
    #             "very": 1,
    #             "brown": 1,
    #             "fox": 1,
    #             ",": 2,
    #             "jumps": 3,
    #             "and": 1,
    #             "over": 1,
    #             "lazy": 1,
    #             "dog": 4,
    #             "!": 1,
    #             "dogdogdog": 1,
    #         })

if __name__ == '__main__':
    unittest.main()