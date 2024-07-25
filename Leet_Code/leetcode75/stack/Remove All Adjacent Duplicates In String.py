class Solution:
    def removeDuplicates(self, s: str) -> str:
        st = []
        for ss in s:

            if st and st[-1] == ss:
                while st and st[-1] == ss:
                    st.pop()
            else:
                st.append(ss)

        return "".join(st)
