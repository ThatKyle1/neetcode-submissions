class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # slow == fast for sure because there is duplicate means there is cycle linked list

        slow2 = 0 # p = x where x is distance from begining of cycle and p before cycle, floyd says p = x and meet where value same
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow == slow2:
                return slow