class Solution(object):
    def arrayChange(self, nums, operations):
        num_indices = {}
        
        for i, num in enumerate(nums):
            num_indices[num] = i
        
        for operation in operations:
            num_to_replace = operation[0]
            replacement = operation[1]
            
            if num_to_replace in num_indices:
                index = num_indices[num_to_replace]
                nums[index] = replacement
                num_indices[replacement] = index
                del num_indices[num_to_replace]
        
        return nums