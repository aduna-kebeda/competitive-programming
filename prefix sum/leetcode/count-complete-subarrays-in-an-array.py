
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        cnt = 0
        dic1 = Counter(nums)
        dic = defaultdict(int)

        left = 0
        c = 0
        for right in range(len(nums)):
            if nums[right] not in dic:
                dic[nums[right]] = 1
            else:
                dic[nums[right]] += 1

            while len(dic) == len(dic1) and left <= right:
                dic[nums[left]] -= 1
                if dic[nums[left]] <= 0:
                    dic.pop(nums[left])
                left += 1
                cnt += 1
    
            c += cnt

        return c
