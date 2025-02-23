from collections import defaultdict
from typing import Counter, List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l, r = 0, len(p)-1
        res = []
        check_list = Counter(p) # {c:1, b:1, a:1}
        counter = defaultdict(int)
        while r < len(s):
            
            val = s[r]
            # 判斷s[r]是不是在check_list裡面, 若不是直接把l, r 跳到 r+1
            if val not in check_list:
                r += 1
                l = r 
                counter = defaultdict(int)
            else:
                # 確認現在
                counter[val] += 1
                # 現在的字母次數一樣且長度一樣
                if counter[val] == check_list[val] and r-l+1 == 


        return res 