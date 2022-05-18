class Solution:

        
    def isPalindrome(self, s: str) -> bool:
        j = len(s)-1
        i = 0
        
        while i < j:
            while i < j and not self.alphaNum(s[i]):
                i = i +1
            while i < j and not self.alphaNum(s[j]):
                j -= 1
                
            if(s[i].lower() != s[j].lower()):
                return False
            i = i + 1
            j = j - 1
        return True
    
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))
sln = Solution()
s = "A man, a plan, a canal: Panama"
s2 = "race a car"
print(sln.isPalindrome(s))
print(sln.isPalindrome(s2))