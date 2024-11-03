from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        st = []

        for i, temperature in enumerate(temperatures):

            while st and temperature > temperatures[st[-1]]:
                j = st.pop()
                res[j] = i - j

            st.append(i)

        return res


Solution().dailyTemperatures([4, 2, 3])
