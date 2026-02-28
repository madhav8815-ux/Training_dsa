# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sp = fp = head

        while fp:
            sp = sp.next
            if fp.next == None:
                return None
            fp = fp.next.next
            if sp == fp:
                break
        else:
            return None

        sp = head

        while sp != fp:
            sp = sp.next
            fp = fp.next

        return fp