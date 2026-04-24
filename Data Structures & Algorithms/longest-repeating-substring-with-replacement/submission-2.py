class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # create a map to hold all uppercase letters
        # then create sliding window to go throughh
        # calculate length - most freq <= k 
        # this means its valid and length is possible
        # if not move left pointer over and re calc map and such and see if update
        hashmap = {}
        result = 0
        l = 0 
        for r in range(len(s)):
            hashmap[s[r]] = hashmap.get(s[r], 0) + 1
            while(r - l + 1 - max(hashmap.values()) > k):
                hashmap[s[l]] = hashmap.get(s[l]) - 1
                l += 1
            result = max(result, r - l + 1)
        return result