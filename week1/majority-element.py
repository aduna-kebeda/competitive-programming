class Solution(object):
    def majorityElement(self, nums):
        n=int(len(nums)/2)
        count = Counter(nums)
        maxi = count.most_common(1)[0][0]
        print(maxi)
        return maxi

        