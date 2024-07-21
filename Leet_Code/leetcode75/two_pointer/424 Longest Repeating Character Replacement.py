class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        res = 0
        L = 0
        remain = k
        check = {}
        for R in range(len(s)):

            if remain == 0 and s[R] != max(check):
                # 若字母已經不能替換了
                # 若不是出現最多的數字
                if s[L] != max(check):
                    remain += 1

                check[s[L]] -= 1
                L += 1

            if s[R] in check:
                check[s[R]] += 1
            else:
                check[s[R]] = 1
                remain -= 1
            res = max(res, R - L + 1)
        return res


Solution().characterReplacement("ABABB", 1)  # 5

Solution().characterReplacement("ABABB", 2)  #
