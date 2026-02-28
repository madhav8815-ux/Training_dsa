
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for data in strs:
            temp = sorted(data)
            temp = "".join(temp)
            if temp in d:
                d[temp].append(data)
            else:
                d[temp] = [data]
        return list(d.values())