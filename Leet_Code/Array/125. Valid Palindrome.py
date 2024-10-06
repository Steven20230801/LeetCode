class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 將整個字串轉換為小寫，以實現不區分大小寫的比較
        s = s.lower()

        # 初始化左指針 (l) 和右指針 (r)
        l, r = 0, len(s) - 1

        # 使用雙指針從字串的兩端向中間移動
        while l <= r:
            # 如果左指針指向的字符不是字母或數字，則左指針向右移動
            if not s[l].isalnum():
                l += 1
                continue  # 繼續下一輪迴圈

            # 如果右指針指向的字符不是字母或數字，則右指針向左移動
            if not s[r].isalnum():
                r -= 1
                continue  # 繼續下一輪迴圈

            # 比較左右指針所指向的字符
            if s[l] != s[r]:
                # 如果不相等，則字串不是迴文
                return False

            # 如果相等，則左右指針分別向中間移動
            l += 1
            r -= 1

        # 如果所有對應的字符都相等，則字串是迴文
        return True


# 創建 Solution 的實例
solution = Solution()

# 測試案例
print(solution.isPalindrome(""))  # True，空字串被視為迴文
print(solution.isPalindrome("A"))  # True，單一字符是迴文
print(solution.isPalindrome("A man, a plan, a canal: Panama"))  # True
print(solution.isPalindrome("race a car"))  # False
print(solution.isPalindrome("No 'x' in Nixon"))  # True
