from collections import Counter

word1 = "aabbcc"
word2 = "ccbbdd"

import math

math.ceil


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        if len(word1) != len(word2):
            return False

        if set(word1) != set(word2):
            return False

        # calculate freq list
        w1 = Counter(word1)
        w2 = Counter(word2)
        f1 = Counter(w1.values())
        f2 = Counter(w2.values())
        if f1 != f2:
            return False

        return True
