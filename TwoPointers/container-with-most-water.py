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
        l=0
        r=len(height)-1
        maxAr=0
        
        while(l<r):
            maxAr=max(maxAr,min(height[l],height[r])*(r-l))
            
            if(height[l]<height[r]):
                l+=1
            else:
                r-=1
        return maxAr
            
        
sln = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(sln.maxArea(height=height))
    