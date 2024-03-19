class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left, right):
            ans=[]
            l,r=0,0
            while l < len(left) and r< len(right):
                if left[l] <= right[r]:
                    ans.append(left[l])
                    l+=1
                else:
                    ans.append(right[r])
                    r+=1
            ans.extend(right[r:])
            ans.extend(left[l:])
            return ans


        def divide(left, right):
            if left==right:
                return nums[left:right+1]

            mid=(left+ right)//2
            left_arr=divide(left, mid)
            right_arr=divide(mid + 1, right)


            return merge(left_arr, right_arr)

        return divide(0, len(nums))






        
        

     

