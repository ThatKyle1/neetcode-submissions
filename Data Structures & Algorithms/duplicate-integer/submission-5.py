class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()
        for i in nums:
            if i not in hashSet:
                hashSet.add(i)
                print(i)
            else:
                return True

        return False