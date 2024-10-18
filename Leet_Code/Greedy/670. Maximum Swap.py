class Solution:
    def maximumSwap(self, num: int) -> int:
        # 將 num 轉換為數字列表
        digits = [int(x) for x in str(num)]

        # 建立一個字典，記錄每個數字（0-9）最後一次出現的位置
        last = {}
        for i, digit in enumerate(digits):
            last[digit] = i

        # 從左到右遍歷數字列表
        for i, digit in enumerate(digits):
            # 嘗試從9到 digit+1 的數字，尋找可以交換的更大數字
            for d in range(9, digit, -1):
                # 如果存在這個數字且其最後出現的位置在當前索引的右側
                if d in last and last[d] > i:
                    # 交換兩個數字
                    digits[i], digits[last[d]] = digits[last[d]], digits[i]
                    # 返回交換後的數字
                    return int("".join(map(str, digits)))

        # 如果無法找到更優的交換方案，返回原數字
        return num

solution = Solution()

# 測試案例 1
num = 2736
print(solution.maximumSwap(num))  # 輸出應為 7236

# 測試案例 2
num = 9973
print(solution.maximumSwap(num))  # 輸出應為 9973

# 測試案例 3
num = 98368
print(solution.maximumSwap(num))  # 輸出應為 98863

# 測試案例 4
num = 0
print(solution.maximumSwap(num))  # 輸出應為 0
