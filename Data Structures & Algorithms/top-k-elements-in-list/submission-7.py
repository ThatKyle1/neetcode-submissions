class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        bucket = [[] for _ in range(len(nums) + 1)]

        for i in nums: # count appearences of each number
            hashmap[i] = 1 + hashmap.get(i, 0)
        
        for num, count in hashmap.items():
            bucket[count].append(num)
        res = []
        
        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res
