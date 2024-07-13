from typing import List


spells = [5, 1, 3]
potions = [1, 2, 3, 4, 5]
success = 7


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()  # 先對potions進行排序, 以便使用二分查找
        # 創建一個新的, success / spells的列表, 這樣之後每個element只要找大於等於此數的位子就好
        spells = [success / spell for spell in spells]

        # 找列表中>=target的第一個下標
        def lower_bound(nums, target):
            # 閉區間
            l, r = 0, len(nums) - 1
            while l <= r:

                mid = (l + r) // 2
                if nums[mid] < target:  # 跟目標符號相反
                    l = mid + 1
                else:
                    r = mid - 1  # 若目前中間值比target大, [1,2 ,3 ,4 ,5 ] , 3 > 1.4
            return l

        ans = [len(potions) - lower_bound(potions, spell) for spell in spells]
        return ans


Solution().successfulPairs(spells, potions, success)
