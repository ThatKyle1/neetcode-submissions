class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} #hashmap for storing each num to use to find two indexs
        for i, num in enumerate(nums): # loop thru using enumerate to keep track of index
            diff = target - num # finding diff the second value that would = to target
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[num] = i
        
        return
