# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # new idea find middle reverse seconmd half of list then just combine 


        # # divde list by 2 reverse by middle
        # prev to mark middle 


        # 0 ,1 ,2, 3
        # 6, 5, 4, 3
        currCount = head
        count = 1
        while currCount:
            currCount = currCount.next
            count += 1
        halfIndex = count // 2
        mid = head
        while halfIndex > 1:
            mid = mid.next
            halfIndex -=  1
        curr = mid.next
        mid.next = None
        # now curr should be correct index at where we need to reverse
        
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        # should reverse list

        # now should jsut combine list and would be right
        first = head
        second = prev
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
   



