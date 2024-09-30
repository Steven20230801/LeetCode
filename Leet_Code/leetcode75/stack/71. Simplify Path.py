class Solution:
    def simplifyPath(self, path: str) -> str:

        path = "/.../a/../b/c//../d/./"
        path = path.split(sep="/")

        st = [""]

        for v in path:

            if not v or v == ".":
                continue

            if v == "..":
                if st and len(st) > 1:
                    st.pop()
                continue

            st.append(v)
        print(st)
        print("/".join(st))

        return st


Solution().simplifyPath("/.../a/../b/c/../d/./")

"/.../b/d"
