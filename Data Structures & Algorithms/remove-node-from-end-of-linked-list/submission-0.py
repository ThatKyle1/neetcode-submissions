# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # need to account for if it loops back use two pass for that

        # create a dummy for the first so can get the head back

        dummy = ListNode(0, head)
        l = dummy
        r = head

        while n > 0:
            r = r.next
            n -= 1
        
        while r:
            l = l.next
            r = r.next
        
        l.next = l.next.next

        return dummy.next
            
            



        