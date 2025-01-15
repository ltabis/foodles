#!/usr/bin/env python3
import sys
from collections import Counter
from operator import itemgetter

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
        list is of size `n`. If n is negative, this function returns an empty string.
    """

    if n < 0:
        return []

    # Make the algorithm case insensitive.
    counter = Counter([word.lower() for word in sentence.split()])

    return sorted(counter.items(), key=lambda item: (-item[1], item[0]))[:n]