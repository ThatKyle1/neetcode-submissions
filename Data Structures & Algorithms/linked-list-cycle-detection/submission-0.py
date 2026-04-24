# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # have a set mark each node if in set then means duplicate means cycle
        hashset = set()
        curr = head
        while curr:
            if curr not in hashset:
                hashset.add(curr)
                curr = curr.next
            else:
                print(curr.val)
                return True
        return False
            

