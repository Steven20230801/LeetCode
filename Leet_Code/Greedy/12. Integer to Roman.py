class Solution:
    def intToRoman(self, num: int) -> str:
        # 定義羅馬數字對應的數值和符號，從大到小排序
        d = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        s = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        res = ""  # 初始化結果字符串

        # 遍歷所有羅馬數字對應的數值
        for i in range(len(d)):
            # 當當前數字可以被d[i]整除時，減去d[i]並添加相應的符號
            while num - d[i] >= 0:
                num -= d[i]
                res += s[i]

        return res  # 返回最終的羅馬數字字符串


Solution().intToRoman(3749)
Solution().intToRoman(58)
