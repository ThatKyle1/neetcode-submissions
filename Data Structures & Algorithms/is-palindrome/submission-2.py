class Solution:
    def isPalindrome(self, s: str) -> bool:
        # create two pointers
        l,r = 0, len(s) - 1 # first and last index

        while l < r: # left < right because if one side is the same whole thing is palindrome
            while l < r and not s[l].isalnum():
                l += 1 # moves past it if not a alphabet
            while l < r and not s[r].isalnum():
                r -= 1 # most past it for right pointer
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        
        return True