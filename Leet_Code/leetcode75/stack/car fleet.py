from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 要先對位置做排序

        # position = [10, 8, 0, 5, 3]
        # speed = [2, 4, 1, 1, 3]
        # target = 12
        p_s = [[p, s] for p, s in zip(position, speed)]
        p_s.sort()

        st = []

        for p, s in p_s[::-1]:
            time = (target - p) / s
            st.append(time)

            if len(st) >= 2 and st[-1] <= st[-2]:
                st.pop()

        return len(st)


Solution().carFleet(position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3], target=12)
