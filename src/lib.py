#!/usr/bin/env python3
import sys

def words_by_frequency(sentence: str, n: int) -> list[(str, int)]:
    """Counts the frequency of words in a sentence, returning n elements by the most
    frequent words, ordered alphabetically. This algorithm is case insensitive.

    Parameters
    ----------
    sentence : str
        The sentence to search words into.
    n : int
        Size of the array containing the words in the return value.

    Returns
    -------
    list : list[(str, int)]
        A sorted list of words and their number of occurrence. The returned
        list is of size `n`.
    """

    if n < 0:
        return []

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