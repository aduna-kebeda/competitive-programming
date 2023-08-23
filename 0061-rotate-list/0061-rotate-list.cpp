class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (!head || k == 0) return head;

        ListNode* temp1 = head;
        int length = 1;
        while (temp1->next != nullptr) {
            length++;
            temp1 = temp1->next;
        }
        
       
        temp1->next = head;
        
        
        k = length - k % length;
        ListNode* newTail = head;
        for (int i = 0; i < k - 1; i++) {
            newTail = newTail->next;
        }
        
        
        ListNode* newHead = newTail->next;
        
        
        newTail->next = nullptr;
        
        return newHead;
    }
};