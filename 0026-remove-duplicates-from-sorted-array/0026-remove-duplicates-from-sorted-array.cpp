class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int k=0;
        if(nums.size()==1)
        {
            nums[0]=nums[0];

            k=1;
        }
        else
        for(int i=0; i<nums.size()-1; i++)
        {
          if(nums[i+1]!=nums[i])
          {
              nums[k]=nums[i];
              k++;
              if(i==nums.size()-2)
              {
                  nums[k]=nums[i+1];
                  k++;
                  
              }
             
          } 
          else{
              if(i==nums.size()-2) 
              {
                  nums[k]=nums[i];
              k++;
              }
          }
        }
        return k;
    }
};