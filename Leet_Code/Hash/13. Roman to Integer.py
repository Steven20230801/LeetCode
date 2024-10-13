class Solution:
    def romanToInt(self, s: str) -> int:
        # 定義特殊的羅馬數字及其對應的整數值
        ds = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        # 定義單個羅馬字母及其對應的整數值
        d1 = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        i = 0  # 初始化索引
        res = 0  # 初始化結果

        # 遍歷整個字符串
        while i < len(s):
            # 檢查當前字符和下一個字符是否組成特殊羅馬數字
            if i < len(s) - 1 and s[i : i + 2] in ds:
                res += ds[s[i : i + 2]]  # 加上特殊數字的值
                i += 2  # 索引跳過兩個字符
            else:
                res += d1[s[i]]  # 加上單個字符的值
                i += 1  # 索引前進一個字符
        return res  # 返回最終結果


Solution().romanToInt("III")
Solution().romanToInt("LVIII")
Solution().romanToInt("MCMXCIV")
