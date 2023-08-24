class Solution(object):
    def merge(self, nums1, m, nums2, n):
        c=0
        for i in range(m, len(nums1)):
            nums1[i]=nums2[c]
            c=c+1
        if len(nums2)>c:
            for j in range(c, len(nums2)):
                nums1.append(nums2[j])

        nums1.sort()

        return nums1