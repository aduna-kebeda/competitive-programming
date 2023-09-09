# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        odd=[]
        even=[]

        temp1=head
        i=1
        while temp1 is not None:
            if i%2==0:
                even.append(temp1.val)
            else:
                odd.append(temp1.val)
            i+=1
            temp1=temp1.next
        temp1=head
        n=len(odd)
        c=0
        while c<n:
            temp1.val=odd[c]
            c+=1
            temp1=temp1.next
        e=0
        n=len(even)
        while e<n:
            temp1.val=even[e]
            e+=1
            temp1=temp1.next
        return head

            

        