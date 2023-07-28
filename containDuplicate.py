class Solution(object):
    def containsDuplicate(self, nums):
       lst=[]
       lst=set(nums)
       if len(nums)>len(lst):
           return True
       else:
           return False
          
       
