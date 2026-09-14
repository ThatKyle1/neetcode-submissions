class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        hashmap = {}
        # hashmap will have number and count
        # another array bucket will be assign count as index, and number as value

        for i in nums:
            hashmap[i] = hashmap.get(i, 0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for number, count in hashmap.items():
            buckets[count].append(number)

        
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                if k > 0:
                    res.append(num)
                    k -= 1
                else:
                    break
        return res
