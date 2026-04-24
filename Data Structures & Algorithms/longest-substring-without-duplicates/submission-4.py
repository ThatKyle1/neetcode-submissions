class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # first create a set bc they cant hold duplicates
        charSet = set()
        l = 0 # create window, left pointer starts at left
        result = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            result = max(result, r - l + 1)
        return result