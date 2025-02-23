from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        l, r = 0, len(arr) - 1

        while r - l + 1 != k:

            if abs(arr[l] - x) <= abs(arr[r] - x):
                r -= 1  # r距離x較遠
            else:
                l += 1

        return arr[l : r + 1]


# binary search
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        l, r = 0, len(arr) - k

        res = -1
        while l <= r:
            mid = (l + r) // 2
            # 計算x ~ arr[mid] 與 x ~ arr[mid+k]

            if mid == n - k or (x - arr[mid] <= arr[mid + k] - x):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return arr[res : (res + k)]


Solution().findClosestElements(arr=[1, 2, 3, 4, 5], k=4, x=3)
Solution().findClosestElements([1, 1, 2, 2, 2, 2, 2, 3, 3], 3, 3)
Solution().findClosestElements(arr=[1, 1, 2, 3, 4, 5], k=4, x=-1)
