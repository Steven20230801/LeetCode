from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        res = 1
        L = 0
        count = {}
        maxf = 0
        for R in range(0, len(s)):

            if s[R] in count:
                count[s[R]] += 1
            else:
                count[s[R]] = 1

            maxf = max(maxf, count[s[R]])
            while R - L + 1 - maxf > k:
                count[s[L]] -= 1
                L += 1

            res = max(res, R - L + 1)
        return res


Solution().characterReplacement("ABABB", 1)  # 5

Solution().characterReplacement("ABABB", 2)  #

# ABB 1
# {A:1}, max A , Remain = 1, res = 1
# {A:1, B:1}, max A, B, Remain = 0, res = 2
# {A:1, B:2}, max B, Remain = 0, res = 3
