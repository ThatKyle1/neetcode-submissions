class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # create set
        numsSet = set(nums)
        longest = 0
        for n in nums:
            if (n-1) not in numsSet: #means begining of seq
                length = 0
                while (n + length) in numsSet:
                    length += 1 
                longest = max(longest, length)
        return longest
# 4 5 6