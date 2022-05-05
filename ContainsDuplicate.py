
from turtle import rt
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
            
        return False
    
    def containsDuplicate2(self, nums: List[int]) -> bool:
        nums.sort()
        for index in range(len(nums)-1):
            if nums[index]==nums[index+1]:
                return True
        
        return False

nums = [1,2,3,1]
sln =  Solution()
print(sln.containsDuplicate2(nums))
nums = [1,2,3,3]
print(sln.containsDuplicate2(nums))
nums = [1,2,3,1]
print(sln.containsDuplicate(nums))
nums = [1,2,3]
print(sln.containsDuplicate(nums))


