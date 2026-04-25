class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        
        # encode for each string num#
        return res

    def decode(self, s: str) -> List[str]:
        
        res, i = [], 0
        while i < len(s):
            j = i # need this if number is liek 23 count both numbers
            while s[j] != "#": 
                j+=1
            length = int(s[i:j])
            i = j + 1
            j = j + 1 + length
            res.append(s[i:j])
            i = i + length

            # 5#hello4#
        return res

