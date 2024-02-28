# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        cnt = 0
        temp = head
        maxi = 0
        while temp:
            maxi += 1
            temp = temp.next
        mod = maxi % k
        size = maxi//k
        arr = []
        temp = head        
        for i in range(k):
            a=0
            lst=ListNode(0)
            partial = lst
            if mod>0:
                mod -=1
                a=1
            for j in range(size+a):
                print(temp.val)
                # lst.ne(ListNode(temp.val))
                lst.next  = ListNode(temp.val)
                lst = lst.next
                temp = temp.next
            arr.append(partial.next)

        return arr

            
