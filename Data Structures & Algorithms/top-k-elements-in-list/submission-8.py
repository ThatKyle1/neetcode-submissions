class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        res = []
        hashmap = {} # will contain all the key,value (number, count)
        # create a list that maps count to the index, and actual number to value

        countIndexLst = [[] for _ in range(len(nums) + 1)]
        
        for i in nums:
            hashmap[i] = 1 + hashmap.get(i, 0)
        
        for number, count in hashmap.items():
            countIndexLst[count].append(number)
        
        for i in range(len(countIndexLst) - 1, -1, -1):
            for num in countIndexLst[i]:
                res.append(num)
                if len(res) == k:
                    return res

        return res
