class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charArray = [0] * 26
        if len(s) != len(t):
            return False
        for char in s:
            index = ord(char) - ord('a')
            print(index)
            charArray[index] += 1
        
        for char in t:
            index = ord(char) - ord('a')
            if charArray[index] > 0:
                charArray[index] -= 1
            else:
                return False
        
        return True
     
