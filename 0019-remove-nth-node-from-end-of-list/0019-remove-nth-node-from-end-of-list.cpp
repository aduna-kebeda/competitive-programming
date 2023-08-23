class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* temp1 = head;
        int c = 0;
        
        if (n == 1 && temp1->next == nullptr)
            return nullptr;

        while (temp1 != nullptr) {
            c++;
            temp1 = temp1->next;
        }
        
        int t = c - n;
        temp1 = head;
        
        if (t == 0) {
            ListNode* newHead = head->next;
            delete head;
            return newHead;
        }
        
        while (t - 1 > 0) {
            temp1 = temp1->next;
            t--;
        }
        
        ListNode* temp2 = temp1->next;
        if (temp1->next != nullptr) {
            temp1->next = temp1->next->next;
        }
        delete temp2;

        return head;
    }
};