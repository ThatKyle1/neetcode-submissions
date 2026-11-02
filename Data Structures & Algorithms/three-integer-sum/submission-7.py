class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        

        # i, j, k cannot be the same

        # my idea: sort nums: create a for loop to loop through each number to not make duplicaes
        # create two pointers after, l and r in that sublist
        # have a target = 0 , move pointers based on 
        # i + l + r > 0, move right pointer, r -= 1
        # i + l + r < 0, move left pointer, l += 1
        # if == 0 returnlist.append(i, l, r)



        nums.sort()
        return_list = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue # for duplicates
            l, r = i + 1, len(nums) - 1
            while l < r: # make sure can't cross
                check = nums[i] + nums[l] + nums[r]
                if check > 0:
                    r -= 1
                elif check < 0:
                    l += 1
                else:
                    return_list.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1 # cant reui0se
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1  # skip duplicate second numbers
        return return_list