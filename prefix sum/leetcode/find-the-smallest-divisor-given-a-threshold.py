class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def isPossible(div):
            cnt=0
            for num in nums:
                cnt+= num//div
                if num%div:
                    cnt+=1
            return cnt<=threshold
        nums.sort()
        low=1
        high=sum(nums)
        while low <= high:
            mid=(low + high)//2
            if isPossible(mid):
                high= mid -1
            else:
                low = mid + 1
        return low
