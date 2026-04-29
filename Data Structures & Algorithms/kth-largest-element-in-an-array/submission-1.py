class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # kth largest give me idea of using a maxHeap


        minHeap = []
        for num in nums:
            heapq.heappush(minHeap, num)
            while len(minHeap) > k:
                heapq.heappop(minHeap)
        return heapq.heappop(minHeap)