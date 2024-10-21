from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 將數組排序
        n = len(nums)
        res = []

        for i in range(n - 2):
            # 早期終止：如果當前數字大於0，後續不可能有三數之和為0
            if nums[i] > 0:
                break

            # 跳過重複的第一個數字
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            x = nums[i]
            l, r = i + 1, n - 1

            while l < r:
                y = nums[l]    
                z = nums[r]
                total = x + y + z

                if total == 0:
                    res.append([x, y, z])
                    l += 1
                    r -= 1

                    # 跳過重複的 y
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    # 跳過重複的 z
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif total < 0:
                    l += 1  # 需要更大的數來增加總和
                else:
                    r -= 1  # 需要更小的數來減少總和

        return res


Solution().threeSum(nums = [-1,0,1,2,-1,-4])
Solution().threeSum(nums = [0,1,1])
Solution().threeSum(nums = [0,0,0])
Solution().threeSum(nums = [-2,0,0,2,2])