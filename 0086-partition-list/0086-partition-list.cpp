/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        ListNode* temp1 = head;
        ListNode* new_node = new ListNode(0);
        new_node->next = nullptr;
        ListNode* temp2 = new_node;

        while (temp1 != nullptr) {
            if (temp1->val <x) {
                ListNode* temp3 = new ListNode(temp1->val);
                if (temp2->next == nullptr) {
                    temp2->next = temp3;
                } else {

                    while(temp2->next!=NULL)
                    {
                    temp2=temp2->next;
                    }
                     temp3->next = NULL;
                     temp2->next = temp3;
                }
            }
            temp1 = temp1->next;
        }

        temp1 = head;  

        while (temp1 != nullptr) {
            if (temp1->val >= x) {
                ListNode* temp3 = new ListNode(temp1->val);
                if (temp2->next == nullptr) {
                    temp2->next = temp3;
                } else {

                    while(temp2->next!=NULL)
                    {
                    temp2=temp2->next;
                    }
                     temp3->next = NULL;
                     temp2->next = temp3;
                }
            }
            temp1 = temp1->next;
        }
        return new_node->next;
    }
};