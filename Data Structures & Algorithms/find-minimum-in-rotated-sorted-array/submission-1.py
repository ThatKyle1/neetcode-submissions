class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r  = 0, len(nums) - 1 # initialize pointers
        result = nums[0]
        while l <= r:
            if nums[l] < nums[r]: # if array sorted
                result = min(result, nums[l])
                break
            mid = (l + r) // 2
            result = min(result, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        
        return result


            