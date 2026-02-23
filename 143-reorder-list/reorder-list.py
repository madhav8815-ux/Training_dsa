# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None or head.next.next is None:
            return
        else: 
            sp = fp = head
            while fp.next and fp.next.next:
                sp = sp.next
                fp = fp.next.next

            temp = sp.next
            sp.next = None

            prev = None
            curr = temp
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            temp = prev

        # merge lists
        start = head
        head = head.next    
        start.next = None
        end = start

        while head and temp:
            end.next = temp
            temp = temp.next
            end = end.next
            end.next = None

            end.next = head
            head = head.next
            end = end.next
            end.next = None

        if temp:
            end.next = temp