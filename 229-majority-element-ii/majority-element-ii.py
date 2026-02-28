
from ast import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        r1 = r2 = None
        c1 = c2 = 0
        for value in nums:
            if r1 == value:
                c1 += 1
            elif r2 == value:
                c2 += 1
            elif c1 == 0:
                r1 = value
                c1 = 1
            elif c2 == 0:
                r2 = value
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1
        
        c1 = c2 = 0
        for v in nums:
            if v == r1:
                c1 += 1
            elif v == r2:
                c2 += 1
        size = len(nums) // 3
        if c1 > size and c2 > size:
            return [r1,r2]
        elif c1 > size:
            return [r1]
        elif c2 > size:
            return [r2]
        else:
            return []
        