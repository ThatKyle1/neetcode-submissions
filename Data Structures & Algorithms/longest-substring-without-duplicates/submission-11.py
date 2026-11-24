class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 1
        l, r = 0, 1
        if len(s) == 0:
            return 0
        seen = set(s[0])
        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l]) # pop until you reach duplicate
                l += 1
            longest = max(longest, r - l + 1)
            seen.add(s[r])
            r += 1
        return longest

            