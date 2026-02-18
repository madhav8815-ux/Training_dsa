# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head == None:
            return None

        h1 = t1 = None   # list for nodes < x
        h2 = t2 = None   # list for nodes >= x

        while head:
            temp = head          # take current node
            head = head.next     # move forward
            temp.next = None     # detach node

            if temp.val < x:
                if h1 == None:
                    h1 = t1 = temp
                else:
                    t1.next = temp
                    t1 = temp
            else:
                if h2 == None:
                    h2 = t2 = temp
                else:
                    t2.next = temp
                    t2 = temp

        # merge both lists
        if h1 == None:
            return h2

        t1.next = h2
        return h1
