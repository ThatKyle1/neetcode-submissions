class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # kth largest give me idea of using a maxHeap

        nums.sort()
        return nums[len(nums) - k]