class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # sort
        # create two pointers - them get count save in array return biggest one
    
        
        res = []

        
        lst = list(set(nums))
        lst.sort()
        print(lst)

        if len(lst) == 0:
            return 0
        elif len(lst) == 1:
            return 1

        l = 0
        for r in range(1,len(lst)):
            
            if lst[r] == lst[r-1] + 1:
                if r == len(lst) - 1:
                    res.append(r - l + 1)
                continue
            else:
                res.append(r - l)
                l = r
                

        return max(res)

        # 1, 2 ,3 , 6, 7