class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        lst = [[] for i in range(len(nums) + 1)] # create a 2d list with length 
        for i in nums:
            hashmap[i] = 1 + hashmap.get(i, 0) # get value if none 0
        for num, count in hashmap.items(): # use buckets
            lst[count].append(num) # creates bucket list listing out
            # each bucket has just one value in it saving least freq to most freq
        result = []
        for i in range(len(nums), -1, -1):
            for n in lst[i]:
                result.append(n)
                print(result)
                if len(result) == k:
                    return result
        
        return result
        
            
            
