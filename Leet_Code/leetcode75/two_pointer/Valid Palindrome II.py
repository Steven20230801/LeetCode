class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        # life = 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                # abbac , 由於不確定要刪除a or c 要兩種方式都確認
                # 1. 檢查abba , 刪除c
                checks = s[l:r]
                check1 = checks == checks[::-1]
                # 2. 檢查bbac , 刪除a
                checks2 = s[l + 1 : r + 1]
                check2 = checks2 == checks2[::-1]
                return check1 or check2

        return True


Solution().validPalindrome("abbac")
