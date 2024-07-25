from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        st = []
        for i in range(len(temperatures)):

            # 若目前stack有資料 且 最後一個比現在的小:
            while st and temperatures[st[-1]] < temperatures[i]:
                # 最外面的跳出來
                x = st.pop()
                ans[x] = i - x

            # 現在得進去
            st.append(i)

        return ans


Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
