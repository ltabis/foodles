#!/usr/bin/env python3
import sys

def words_by_frequency(sentence: str, n: int) -> dict[str, int]:
    # Make the algorithm case insensitive.
    words = [word.lower() for word in sentence.split()]

    dict = {}
    for word in words:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1

    by_alpha = sorted(dict.items(), key=lambda item: item[0])
    by_value = sorted(by_alpha, key=lambda item: item[1], reverse=True)

    return by_value[:n]