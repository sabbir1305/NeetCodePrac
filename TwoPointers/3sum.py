from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        nums.sort()
        for i , a in enumerate(nums):
            if i>0 and a == nums[i-1]:
                l , r = i+1 , len(nums)-1
                while l < r:
                    s = a + nums[l] + nums[r]
                    if s > 0:
                        r -= 1
                    elif s < 0:
                        l += 1
                    else:
                        result.append([a, nums[l],nums[r]])
                        l += 1
                        while nums[l] == nums[l-1] and l < r:
                            l += 1
        return result

sln = Solution()
nums = [-1,0,1,2,-1,-4]
print(sln.threeSum(nums))
          
            
         
       