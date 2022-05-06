from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words={}
        for word in strs:
            s =''.join(sorted(word))
            if s in words:
                words[s].append(word)
            else:
                words[s]=[word]
        return [words[s] for s in words ]
    
    def groupAnagrams2(self, strs:list[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for str in strs:
            count = [0] * 26
            
            for c in str:
                count[ord(c) - ord('a')] += 1
            
            res[tuple(count)].append(str)
        return res.values() 