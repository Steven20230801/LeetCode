from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for s in asteroids:

            while st and st[-1] > 0 and s < 0:
                if st[-1] + s > 0:
                    break
                elif st[-1] + s == 0:
                    st.pop()
                    break
                else:
                    st.pop()
            else:
                st.append(s)

        return st


Solution().asteroidCollision([5, -6])
