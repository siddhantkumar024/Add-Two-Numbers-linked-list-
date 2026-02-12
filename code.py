# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sid=ListNode()
        curr=sid
        c=0
        while l1 or l2 or c:
            v1=l1.val if l1 else 0
            v2=l2.val if l2 else 0
            # cal total value with carry at start carry is 0
            t= v1+v2+c
            # if val is greater than 10 then carry will change
            c=t//10
            # creating new node and storing val as first node is sid
            curr.next=ListNode(t%10)
            curr=curr.next
            if l1 :
                l1=l1.next
            if l2:
                l2=l2.next
        return sid.next

        
