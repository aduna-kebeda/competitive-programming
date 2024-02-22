class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[-1]*(len(nums1))
        dic=defaultdict(int)
        for i in range(len(nums2)):
            dic[nums2[i]]=i
        for i in range(len(nums1)):
            j=dic[nums1[i]]
            while j<len(nums2):
                if nums2[j]>nums1[i]:
                    result[i]=nums2[j]
                    break
                j+=1
        return result
