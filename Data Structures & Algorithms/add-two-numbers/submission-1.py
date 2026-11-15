# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # create a function to reveerse both the linked list
        def reverse(lst):
            curr = lst
            prev = None
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            return prev

        rL1 = reverse(l1) # reverse liniked list head
        rL2 = reverse(l2) # reversed linked list
        stringL1 = ""
        stringL2 = ""
        while rL1:
            stringL1 += (str(rL1.val))
            rL1 = rL1.next

        while rL2:
            stringL2 += (str(rL2.val))
            rL2 = rL2.next
        
        addedNum = int(stringL1) + int(stringL2) # int of the added nums
        addedNumString = str(addedNum)
        dummy = ListNode()
        tail = dummy
        for num in reversed(addedNumString):
            tail.next = ListNode(int(num))
            tail = tail.next

        return dummy.next


        
        