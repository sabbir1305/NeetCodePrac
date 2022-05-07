from itertools import count
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = {}
        freq = [[] for i in range(len(nums) + 1)
                ]
        for n in nums:
            numCount[n] = 1 + numCount.get(n,0) 
        for n,c in numCount.items():
            freq[c].append(n)
            
        res = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

sln = Solution()
nums = [1,1,1,2,2,3]
k = 2   
print(sln.topKFrequent(nums=nums,k=2))