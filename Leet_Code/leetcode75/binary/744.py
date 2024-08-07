from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        l, r = 0, len(letters) - 1

        # 找比target大的第一個數字
        while l <= r:

            mid = (l + r) // 2
            if letters[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1

        if l >= len(letters):
            return letters[0]
        else:
            return letters[l]


Solution().nextGreatestLetter(["x", "x", "y", "y"], "z")
