from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        h1 = {}
        h2 = {}
        if len(word1) != len(word2):
            return False

        for i in range(len(word1)):

            if word1[i] not in h1:
                h1[word1[i]] = 1
            else:
                h1[word1[i]] += 1

            if word2[i] not in h2:
                h2[word2[i]] = 1
            else:
                h2[word2[i]] += 1

        # check key and value are same
        if h1.keys() == h2.keys() and Counter(h1.values()) == Counter(h2.values()):
            return True
        else:
            return False


Solution().closeStrings("cabbba", "abbccc")
Solution().closeStrings("abc", "cba")

Solution().closeStrings("a", "aa")
