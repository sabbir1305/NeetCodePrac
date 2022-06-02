

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        sub_string_set = set()
        for r in range(len(s)):
            while s[r] in sub_string_set:
                sub_string_set.remove(s[l])
                l +=1
            sub_string_set.add(s[r])
            res = max(res,r-l+1)
        return res

s = "abcabcbb"
sln = Solution()
print('__:',sln.lengthOfLongestSubstring(s))