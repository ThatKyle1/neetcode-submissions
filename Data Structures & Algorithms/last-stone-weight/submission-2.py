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
            first = heapq.heappop(maxHeap) # gets first largest
            second = heapq.heappop(maxHeap) # gets second largest

            if first != second:
                heapq.heappush(maxHeap, first - second)
        
        if len(maxHeap) > 0:
            return -maxHeap[0]
        
        return 0