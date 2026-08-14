# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        count=0
        while curr:
            curr=curr.next
            count+=1
        sem=count-(n+1)
        if n==count:
            return head.next
        ab=head
        for i in range(sem):
            ab=ab.next
        ab.next=ab.next.next
        return head


            

    