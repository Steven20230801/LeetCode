from typing import List


[5,10,-5, 5, -12, 9]

[5, 10]
[5, 10]
[5, 10, 5]
[-12] 


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        
        ans.append(asteroids[0])
        
        for r in range(len(asteroids)):
            
            if r and r[-1] 