from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numDict = {}
        for i in range(0,len(numbers)):
            remain = target - numbers[i]
            if numbers[i] in numDict.keys():
                return [numDict[numbers[i]]+1,i+1]
            else :
                numDict[remain] = i
    
    def twoSumWithPointer(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        while (l < r):
            currentSum =  numbers[l] + numbers[r]
            if currentSum==target:
                return [l+1,r+1]
            elif (currentSum > target):
                r -= 1
            else:
                l +=1
            
            
            
            
sln = Solution()
numbers = [2,3,4]
target = 6          
print(sln.twoSumWithPointer(numbers=numbers,target=target))