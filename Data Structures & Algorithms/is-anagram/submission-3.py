class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sL = list(s)
        tL = list(t)
        if sorted(sL) != sorted(tL) :
            return False

        return True