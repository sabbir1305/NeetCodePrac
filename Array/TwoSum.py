from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} #val : index
        
        for index , number in enumerate(nums):
            diff = target - number
            print('index ',index)
            print('number ',number)
            if diff in prevMap:
                return [prevMap[diff], index]
            prevMap[number] = index

sln = Solution()
print(sln.twoSum([2,7,11,15],26))