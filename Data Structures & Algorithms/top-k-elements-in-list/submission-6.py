class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # create a hashmap that stores all the nums as key, and count as value
        buckets = [[] for _ in range(len(nums) + 1)]
        result = []
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1
        
        # idea loop through key,value, save count as index in buckets and put the key(number) there
        # thus when sorting backwards it should be in correct order

        for index, count in count.items():
            buckets[count].append(index)
        print(buckets)

        for bucket in reversed(buckets):
            for num in bucket:
                if len(result) < k:
                    result.append(num)
                else:
                    return result
        return result



        
            
            
