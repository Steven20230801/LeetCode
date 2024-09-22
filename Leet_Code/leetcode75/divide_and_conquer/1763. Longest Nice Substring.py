from collections import Counter


class Solution:

    def check_nice(self, s) -> bool:
        counter = Counter(s)

        for s in counter:
            if counter[s] > 0:
                if s.lower() not in counter or s.upper() not in counter:
                    return False
        return True

    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)

        res = []
        l, r = 0, 0

        for l in range(n):
            for r in range(n + 1):
                if self.check_nice(s[l:r]):
                    res.append([l, r - l])

        result = max(res, key=lambda x: (x[1], -x[0]))
        # return result
        return s[result[0] : result[0] + result[1]]


Solution().longestNiceSubstring("aAa")
Solution().longestNiceSubstring("YazaAay")
Solution().longestNiceSubstring("BbBbb")
# Solution().check_nice("a")
