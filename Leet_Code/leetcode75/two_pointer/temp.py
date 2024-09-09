class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)- 1
        life = 1
        while l < r and life >= 0:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                if s[l+1] == s[r] and s[l+1] == s[r]:
                    life -= 1
                    # l += 2
                    r -= 1
                    continue 
                # if s[l] == s[r-1]:
                #     life -= 1
                #     l += 1
                #     r -= 2
                #     continue
                if s[l+1] == s[r]:
                    life -= 1
                    l += 2
                    r -= 1
                    continue 
                if s[l] == s[r-1]:
                    life -= 1
                    l += 1
                    r -= 2
                    continue
                return False
        if life < 0:
            return False
        else:
            return True
                
                
                
Solution().validPalindrome("deeee")

x = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
print(x)
print(x[::-1])