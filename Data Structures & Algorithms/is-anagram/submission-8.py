class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        lstS = [0] * 26

        for char in s:
            index = ord(char) - ord('a')
            lstS[index] += 1
        
        for char in t:
            index = ord(char) - ord('a')
            if lstS[index] > 0:
                lstS[index] -= 1
            else:
                return False
        return True