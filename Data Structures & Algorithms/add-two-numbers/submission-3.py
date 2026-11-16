# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 321
        # 654 # case 1 no carry

        # 151
        # 256 # case 2 carry

        # 1511
        # 151


        
        # they give in reverse order so you can treat it as one pass solve
        # going reverse order just save the carry if any
        dummy = ListNode()
        tail = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            combined = (v1 + v2 + carry) # 18 
            carry = combined // 10 # 16 //10 = 1 
            tail.next = ListNode(combined % 10) # 8
            tail = tail.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next





