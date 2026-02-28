
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for data in nums:
            if data in d :
                d[data ] += 1
            else:
                d[data] = 1
        for key in d:
            if d[key] > len(nums) // 2:
                return key