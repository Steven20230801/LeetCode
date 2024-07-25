class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        st = []  # nest list
        # st = [[b, 1], [a, 1]]...
        for ss in s:
            if st and st[-1][0] == ss:
                st[-1][1] += 1
            else:
                st.append([ss, 1])

            if st[-1][1] == k:
                st.pop()

        return "".join([s[0] * s[1] for s in st])


Solution().removeDuplicates(s="abcd", k=2)
