# Two Pointers 同向双指针

# [0  -------------- i  ------ j ---------------- n]
#   處理完畢且不需要的    未處理    已處理 & 需要的

# 通用步驟
# 1. 初始化左指針 i = 0 以及右指針 j = 0
# 2. 當右指針還沒到達終點時，不斷移動右指針來擴大窗口，同時更新窗口的信息
# 3. 當窗口包含的元素符合條件時，開始移動左指針來縮小窗口，同時更新窗口的信息
# 4. 不斷重複步驟 2 和步驟 3，直到右指針到達終點


# 125. Valid Palindrome
from typing import List


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        for i in range(len(numbers)):
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                right = right - 1
            else:
                left = left + 1
