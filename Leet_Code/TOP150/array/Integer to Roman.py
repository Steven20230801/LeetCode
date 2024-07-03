from typing import List


class Solution:
    def intToRoman(self, num: int) -> str:
        VALUE_SYMBOLS = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]

        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        s = ""
        while num > 0:
            for i in range(len(nums)):
                k = num // nums[i]
                s = s + romans[i] * k
                num = num - nums[i] * k

        return s


Solution().intToRoman(30)  # xxx
Solution().intToRoman(49)  # XLIX


s = "fdfs fsdf   "


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(" ")
        return len(s[-1])


strs = ["flower", "flow", "flight"]


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 0:
            return ""

        ans = strs[0] # 假設第一個字串就是公共前墜
        for i in range(len(ans)):
            # 跟每個str第一個字比較
            for ele in strs[1:]:
                if i >= len(ele): # 若超出長度了代表目前前墜就是最長了
                    return ans[:i]
                if ans[i] != ele[i]: # 若比對不一樣了就直接返回
                    return ans[:i]
        return ans


strs = ["flower", "flow"]
strs = ["flower", "flow", "flight"]

strs = ["dog", "racecar", "car"]
Solution().longestCommonPrefix(strs)


prices = [7, 1, 5, 3, 6, 4]


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 只要有利潤了 就賣出再買進
        cum_profit = 0
        for day in range(1, len(prices)):
            if prices[day] - prices[day-1] > 0:
                cum_profit += prices[day] - prices[day - 1]
        return cum_profit
prices = [7, 6, 4, 3, 1]
Solution().maxProfit(prices)
