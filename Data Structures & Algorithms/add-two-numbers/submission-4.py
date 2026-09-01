# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        num2 = ""

        curr = l1
        curr2 = l2

        while curr:
            num1 = num1+str(curr.val)
            curr = curr.next

        while curr2:
            num2 = num2+str(curr2.val)
            curr2 = curr2.next

        num3 = int(num1[::-1])+int(num2[::-1])
        num3 = str(num3)[::-1]

        dummy = ListNode()
        current = dummy

        for c in num3:
            current.next = ListNode(int(c))
            current = current.next
            
        return dummy.next





