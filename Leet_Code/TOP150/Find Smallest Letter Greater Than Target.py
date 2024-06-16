# 744


from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        while left <= right:
            mid = (left + right) // 2

            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        if letters[right + 1] > target:
            return letters[right + 1]
        else:
            return letters[0]


Solution().nextGreatestLetter(letters=["c", "f", "j"], target="c")


Solution().nextGreatestLetter(letters=["x", "x", "y", "y"], target="z")
