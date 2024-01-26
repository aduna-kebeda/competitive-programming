from collections import defaultdict
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dic = defaultdict(int)
        temp = head
        i = 0
        po = -1

       
        while temp:
            if temp in dic:
                po = dic[temp]
                break

            dic[temp] = i
            temp = temp.next
            i += 1

        temp2 = head
        while po > 0:
            temp2 = temp2.next
            po -= 1

        return temp2 if po != -1 else None
