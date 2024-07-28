from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        cols = list(zip(*matrix))[0]

        def search(nums, target):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2

                if mid == target:
                    return True
                elif mid < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return l - 1

        ft = search(cols, target)

        if ft is True:
            return True
        else:
            if search(matrix[ft], target) is True:
                return True
            else:
                return False


Solution().searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=12)
