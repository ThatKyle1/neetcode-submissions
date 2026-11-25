class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # needs to be a conditon where count of replacement 
        # idea allows window to move to the right if k > 0 
        # if k < 0 : and next letter cant be replaced move sliding window
        # move left pointer by one check before though and remove

        count = {}
        maxfreq = 0
        l = 0
        result = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0) # add 1, 0 if not exist
            # get max freq
            for freq in count.values():
                maxfreq = max(maxfreq, freq)

            # formula for if window is valid , len(window) - maxfreq ) <= k
            while ((r - l + 1) - maxfreq > k): # if not valid move left pointer
                count[s[l]] = count.get(s[l]) - 1
                l += 1
            # once out of loop or not run window is valid
            result = max(result, (r - l + 1))  # r - l + 1 window length
        
        return result