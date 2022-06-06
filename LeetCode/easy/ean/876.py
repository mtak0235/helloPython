# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = middle = head
        n = middle_index = 0
        while curr:
            n += 1
            if middle_index < n // 2:
                middle_index += 1
                middle = middle.next
            curr = curr.next
        return middle
