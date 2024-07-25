from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for i in nums:
            counter[i] = counter.get(i, 0) + 1

        freq = {}
        for s, v in counter.items():
            if v in freq:
                freq[v].append(s)
            else:
                freq[v] = [s]

        freq_list = sorted(freq, reverse=True)

        res = []
        for v in freq_list:
            if k > 0:
                res.extend(freq[v])
                k -= len(freq[v])
            else:
                break
        return res
