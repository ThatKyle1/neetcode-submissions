class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # idea, create two pointers l and r
    
        # left start at begining r start at end 

        # if l + r > target, move r pointer 
        # elif l + r < target, move left pointer
        # l + r == target return l + 1, r + 1
        # one index so remember + 1 to index

        l, r = 0, len(numbers) - 1

        while l < r:
            if (numbers[l] + numbers[r]) > target:
                r -= 1
            elif (numbers[l] + numbers[r]) < target:
                l += 1
            else:
                return [l+1, r+1]
        
        return False

