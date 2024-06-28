from typing import List

spells = [3, 5]
success = 8


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:

        # xy >= success
        # x >= success / y
        # x +1 => success // y
        spells = [success / x for x in spells]
        potions.sort()

        def search_right(target, nums):
            l, r = 0, len(nums) - 1

            while l <= r:
                mid = (l + r) // 2

                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1

            if nums[r] == target:
                return len(nums) - l
            if r > len(nums):
                return 0
            return len(nums) - l

        return [search_right(spell, potions) for spell in spells]


Solution().successfulPairs(spells=[5, 1, 3], potions=[1, 2, 3, 4, 5], success=7)

Solution().successfulPairs(spells=[3, 1, 2], potions=[8, 5, 8], success=16)


# 找大於等於target的nums
def search_right(target, nums):
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1

    if nums[r] == target:
        return r
    return l


search_right(1.4, [1, 2, 3, 4, 5])
search_right(8, [5, 8, 8])
