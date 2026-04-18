class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp = []
        output = False
        for i in nums: 
            if (i in temp):
                output = True
                break
            else:
                temp.append(i)
        return output