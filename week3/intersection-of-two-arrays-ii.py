class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic1=Counter(nums1)
        dic2=Counter(nums2)
        
        nums1=set(nums1)
        nums2=set(nums2)
        num=nums1 & nums2
        result=[]
        for n in num:
            f=min(dic1[n], dic2[n])
            for i in range(f):
                result.append(n)
        
        return result