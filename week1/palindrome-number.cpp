class Solution {
public:
    bool isPalindrome(int x) {
        bool pal=false;
        if(x<0)
        {
          pal=false;
        }
        else
        {
          int n=x;
            long long rev=0;
            while(n!=0)
            {
              rev=((rev*10)+(n%10));
              n=n/10;
            }
            if(x==rev)
             {
                pal=true;
             }
             
        }
          return pal;
    }
};