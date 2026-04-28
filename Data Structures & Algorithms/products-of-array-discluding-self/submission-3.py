class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        seenZeros = 0
        product = 1
        for i in nums:
            if i == 0:
                seenZeros+=1
            else:
                product = product * i

        res = []
        for i in range(len(nums)):
            if seenZeros > 1:
                res.append(0)
            elif seenZeros == 1:
                if nums[i] == 0:
                    res.append(product)
                else:
                    res.append(0)
            else:
                resProduct = int(product / nums[i])
                res.append(resProduct)


        return res