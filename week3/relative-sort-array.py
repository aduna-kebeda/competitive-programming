class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:  
        result = []
        cnt = Counter(arr1)

        for num in arr2:
            result.extend([num] * cnt[num])
        arr2=set(arr2)
        num2 = [num for num in arr1 if num not in arr2]
        num2.sort()
        result.extend(num2)

        return result
