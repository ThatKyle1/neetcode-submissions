class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0
        product = 1
        for i in nums:
            if i == 0:
                zeros += 1
            else:
                product = product * i

        res = []
        
        

        
        for i in nums:
            if zeros > 1:
                res.append(0)
            elif zeros == 1:
                if i == 0:
                    res.append(product)
                else:
                    res.append(0)
            else:
                res.append(int(product / i))
        
        return res