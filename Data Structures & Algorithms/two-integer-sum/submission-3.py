class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
            

        # complement = target - num,
        # loop through nums, save number as key, index as value
        # if complment is in seen, return complment index and num index

