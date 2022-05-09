# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        right = left = head
        while n:
            right, n = right.next, n - 1
        while right and right.next:
            right, left = right.next, left.next
        delNode = left.next
        if not right:
            temp = head
            head = head.next
        else:
            temp = left.next
            left.next = temp.next
        del temp
        return head
