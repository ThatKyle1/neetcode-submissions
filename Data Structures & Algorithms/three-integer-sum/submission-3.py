class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # sort array first
        print(nums)
        lst = []
        # loop through first
        for i, num in enumerate(nums): # loop through every one
            if i > 0 and num == nums[i-1] : # if duplicate
                continue # go to next i
            l,r = i + 1, len(nums) - 1
            while l < r:
                three_sum = nums[l] + nums[r] + num
                if three_sum == 0:
                    print([num, nums[l], nums[r]])
                    lst.append([num, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

                elif nums[l] + nums[r] + num > 0:
                    r -= 1
                elif nums[l] + nums[r] + num < 0:
                    l += 1
        return lst
                    
