class Solution:
    def findMin(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        ans = float("inf")
        while left <= right:
            # if right-left==1:
            #    if nums[right] >nums[left]:
            #        return nums[left]
            #    else:
            #        return nums[right]
            mid = (left + right)//2
            if nums[mid] >= nums[-1]:
                ans = min(ans, nums[mid])
                left= mid +1
            else:
                ans = min(ans, nums[mid])
                right = mid -1
        # print(left, right, ans)   
        return ans