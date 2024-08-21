from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st = []
        l = 0

        for e in pushed:  # PUSH

            st.append(e)

            while l < len(popped) and popped[l] in st:  # POP

                if st[-1] != popped[l]:
                    return False
                else:
                    st.pop()

                l += 1

        return True if not st else False


Solution().validateStackSequences(pushed, popped)
