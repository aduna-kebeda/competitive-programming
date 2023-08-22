class Solution {
public:
    bool isPalindrome(ListNode* head) {
       vector<char> v;

       ListNode* temp1=head;
       while(temp1!=NULL)
       {
        v.push_back(temp1->val);
           temp1=temp1->next;
       }

      vector<char> rev=v;
       reverse(rev.begin(), rev.end());

      return rev==v;
    }

   
};