class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # k elements, so two heaviest stones
        maxHeap = []

        # so if equal pop twice from top
        # if x < y; pop biggest one, then set next one = biggest - second biggest


        # first we need to create out maxHeap


        for num in stones:
            heapq.heappush(maxHeap, -num)
        # now max heap with - should be here

        while(len(maxHeap) > 1):
            if maxHeap[0] == maxHeap[1]: # if equal
                heapq.heappop(maxHeap)
                heapq.heappop(maxHeap)
            else: # if one bigger
                temp = heapq.heappop(maxHeap) # save first val, and pop largest
                newWeight = temp - maxHeap[0] # save new val
                heapq.heappop(maxHeap) # pop second biggest val
                heapq.heappush(maxHeap, newWeight)
        
        if len(maxHeap) > 0:
            return -maxHeap[0]
        
        return 0