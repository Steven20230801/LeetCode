from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # 从第二个元素开始遍历，因为第一个元素默认有序
        for i in range(1, len(nums)):
            key = nums[i]  # 当前要插入的元素
            j = i - 1
            # 从已排序部分的末尾开始向前扫描，找到合适的位置插入
            while j >= 0 and nums[j] > key:
                nums[j + 1] = nums[j]  # 将大于key的元素向后移
                j -= 1
            nums[j + 1] = key  # 在合适的位置插入key
        return nums


class Solution:
    def sortArray(self, N: List[int]) -> List[int]:
        L = len(N)
        for i in range(1, L):
            for j in range(0, i):
                if N[i] < N[j]:
                    N.insert(j, N.pop(i))
                    break
        return N


Solution().sortArray([2, 1, 1, 5])
