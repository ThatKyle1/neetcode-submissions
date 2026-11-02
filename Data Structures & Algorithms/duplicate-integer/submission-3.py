class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() # set for O(1) look ups
        for i in nums:
            if i in seen:
                return True
            else:
                seen.add(i)
        return False

        