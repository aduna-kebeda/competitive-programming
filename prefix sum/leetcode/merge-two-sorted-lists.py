# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1=list1
        p2=list2
        head=None
        temp=head
        while p1 or p2:
            v1=p1.val if p1 else float('inf')
            v2=p2.val if p2 else float('inf')
            print(v1,v2)
            if v1<v2:
                newNode=ListNode(v1)
                p1=p1.next
            else:
                newNode=ListNode(v2)
                p2=p2.next
            if temp:
                   temp.next=newNode
                   temp=temp.next
            else:
                    head=newNode
                    temp=head
           
        return head
        # if p1:
        #     while p1:
        #         newNode=ListNode(p1.val)
        #         newNode.next=None
        #         temp.next=newNode
        #         if temp:
        #            temp.next=newNode
        #            temp=temp.next
        #         else:
        #             temp=newNode
        #             head=temp
              
        #         p1=p1.next
        # else:
        #     while p2:
        #         newNode=ListNode(p2.val)
        #         newNode.next=None
                
        #         if temp:
        #            temp.next=newNode
        #            temp=temp.next
        #         else:
        #             temp=newNode
        #             head=temp
                    
        #         p2=p2.next
        # return head




