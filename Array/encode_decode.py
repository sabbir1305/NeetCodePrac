class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        eStr=""
        for s in strs:
            eStr = eStr  +str(len(s)) +"#"+s
            
        return eStr


    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        i = 0
        res = list()
        while i < len(str):
            j = i
            while str[j]!="#":
                j += 1
            length = int(str[i:j])
            
            res.append(str[j+1:j+1+length])
            i = j+1+length
            
       
        return res

Input = ["lint","code",";:","love","you"]
sln = Solution()
eStr = sln.encode(Input)
print(eStr)
dStr = sln.decode(eStr)
print(dStr)