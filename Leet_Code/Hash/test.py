class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        h = {}
        for r in range(len(s)):
            if s[r] not in h:
                h[s[r]] = t[r]
            else:
                if (
                    h[s[r]] != t[r]
                ):  # 若s[r]已經在h裡面，但是對應的t[r]不等於h[s[r]]，代表不是isomorphic
                    return False

        # 檢查h的value是否有重複
        if len(set(h.values())) != len(h):
            return False
        else:
            return True


Solution().isIsomorphic("aab", "abc")
Solution().isIsomorphic("ab", "aa")
Solution().isIsomorphic("abab", "baba")


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t, t2s = {}, {}
        for ss, tt in zip(s, t):
            if (ss in s2t and s2t[ss] != tt) or (tt in t2s and t2s[tt] != ss):
                return False
            s2t[ss] = tt
            t2s[tt] = ss
        return True


Solution().isIsomorphic("aab", "abc")
Solution().isIsomorphic("ab", "aa")


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        words = s.split()
        if len(pattern) != len(words):
            return False

        p2w, w2p = {}, {}
        for p, w in zip(pattern, words):
            if (p in p2w and p2w[p] != w) or (w in w2p and w2p[w] != p):
                return False
            p2w[p] = w
            w2p[w] = p
        return True
