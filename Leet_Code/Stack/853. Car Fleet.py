from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # target = 12
        # position = [10, 8, 0, 5, 3]
        # speed = [2, 4, 1, 1, 3]
        hours = [(p, (target - p) / s) for p, s in zip(position, speed)]
        hours.sort()
        st = []
        for i in range(len(hours) - 1, -1, -1):
            # 該台到目的地的時間
            s = hours[i][1]
            while st and s <= st[-1]:
                st.pop()

            st.append(s)

            print(st)

        return len(st)


Solution().carFleet(target=12, position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3])
Solution().carFleet(target=10, position=[0, 4, 2], speed=[2, 1, 3])
