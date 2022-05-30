import numbers
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # res = 0
        # for i in range(len(height)):
        #     r = i + 1
        #     while r < len(height):
        #         area = min(height[i],height[r]) * (r-i)
        #         res = max(res,area)
        #         r += 1
        #     i += 1
        #sreturn res
        l,r = 0, len(height) - 1
        maxArea = 0
        while l<r:
            maxArea = max(maxArea, (r-l) * min(height[l],height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxArea
            
        
            
        
sln = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(sln.maxArea(height=height))
    