from typing import Counter, List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # cur 用於當前遍歷指針，l 用於放置 0 的位置，r 用於放置 2 的位置
        cur, l, r = 0, 0, len(nums) - 1

        # 當前指針 cur 必須小於或等於 r，確保不會越界
        while cur <= r:
            if nums[cur] == 0:
                # 如果當前元素是 0，交換它和 l 指向的元素
                nums[cur], nums[l] = nums[l], nums[cur]
                cur += 1  # 移動當前指針到下一個元素
                l += 1  # 將 l 向右移動，表示 0 的下一個位置
                continue  # 繼續下一輪循環，無需檢查 cur 指針的當前元素
            elif nums[cur] == 1:
                # 如果當前元素是 1，只需移動當前指針
                cur += 1
            else:
                # 如果當前元素是 2，交換它和 r 指向的元素
                nums[cur], nums[r] = nums[r], nums[cur]
                r -= 1  # 將 r 向左移動，表示 2 的下一個位置
                # 注意：此時不增加 cur，因為交換後需要檢查新的 nums[cur]


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = Counter(nums)

        cur = 0
        for k in [0, 1, 2]:
            freq = counter.get(k)
            if freq:
                for _ in range(freq):
                    nums[cur] = k
                    cur += 1


Solution().sortColors([1, 1, 0, 0, 2, 2])
