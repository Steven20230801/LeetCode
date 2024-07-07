class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l, r, a = 0, 0, 0
        for r in range(0, k):
            if s[r] in set(["a", "e", "i", "o", "u"]):
                a += 1
        max_sum = a

        # 開始移動窗口
        for r in range(k, len(s)):
            # 確認右邊是不是 +=1
            if s[r] in set(["a", "e", "i", "o", "u"]):
                a += 1
            # 確認左邊是不是 -=1
            if s[l] in set(["a", "e", "i", "o", "u"]):
                a -= 1
            max_sum = max(max_sum, a)
            l += 1

        return max_sum


s = "abciiidef"
k = 3
print(Solution().maxVowels(s, k))

s = "weallloveyou"
k = 7
print(Solution().maxVowels(s, k))


# 2.


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l, r, a = 0, 0, 0
        for r in range(0, k):
            if s[r] in "aeiou":
                a += 1
        max_sum = a

        # 開始移動窗口
        for r in range(k, len(s)):
            # 確認右邊是不是 +=1
            if s[r] in "aeiou":
                a += 1
            # 確認左邊是不是 -=1
            if s[l] in "aeiou":
                a -= 1
            max_sum = max(max_sum, a)
            l += 1

        return max_sum
