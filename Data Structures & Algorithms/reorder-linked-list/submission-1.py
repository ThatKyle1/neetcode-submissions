# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # find middle of the list, sort the right side inverted and merge them

        # find middle using f and slow pointer

        fast, slow = head, head # start both at beginning

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        rlst = slow.next
        # now rlst is begining of right lst
        # we need reverse the rlst
        prev = None
        while rlst:
            temp = rlst.next
            rlst.next = prev
            prev = rlst
            rlst = temp
        
        # now prev should be reversed
        # remove pointer from left list bc dont want point back to something
        slow.next = None
        l, r = head, prev

        while l and r:
            temp1 = l.next
            temp2 = r.next
            l.next = r
            r.next = temp1
            l = temp1
            r = temp2

        # 0, 6, 1, 5, 2, 4, 3
        # 0  n  0  n  0  n  0

        