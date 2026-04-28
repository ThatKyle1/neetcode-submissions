class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # binary search but a little different

        #once you get mid
        # if mid > target and low < target: target must exist in left part of lsit move mid update r = mid - 1
        # if mid > target and low > target: target must exist in right part of list move mid update l + mid 

        low, high = 0, len(nums) - 1
        while low <= high: # if cross number not fouind
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            

            # we need to check if in left sorted or right sorted
            if nums[low] <= nums[mid]:
                if target > nums[mid]:
                    low = mid + 1
                elif target < nums[low]:
                    low = mid + 1
                else:
                    high = mid - 1
            else: # in right
                if target < nums[mid]: # go left tree
                    high = mid - 1
                elif target > nums[high]: # go left tree
                    high = mid - 1
                else:
                    low = mid + 1



        return -1