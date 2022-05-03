class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sLen = len(s)
        tLen = len(t)
        
        if (sLen != tLen ):
            return False
        sCharList = list(s)  
        tCharList = list(t) 
        sCharList.sort()
        tCharList.sort()
        
        for i in range(sLen):
            if(sCharList[i]!= tCharList[i]):
                return False
        
        return True
    
    def isAnagram2(self, s:str , t:str) -> bool:
        
        if len(s) != len(t):
            return False
        countOfS,countOfT = {}, {}
        
        for i in range(len(s)):
            countOfS[s[i]] = 1 + countOfS.get(s[i], 0)
            countOfT[t[i]] = 1 + countOfT.get(t[i], 0)
        for c in countOfS:
            if countOfS[c] != countOfT.get(c, 0):
                return False
        return True
        
    def isAnagram3(self, s:str , t:str) -> bool:
            
        return sorted(s) == sorted(t)
    
sln = Solution()
s = "anagram"
t = "nagaram"

print(sln.isAnagram(s=s,t=t)) 
print(sln.isAnagram2(s=s,t=t)) 
print(sln.isAnagram3(s=s,t=t)) 
             
        