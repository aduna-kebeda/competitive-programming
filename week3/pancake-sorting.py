class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []
        p = len(arr) - 1
        while p > -1:
            maxi = max(arr[:p+1])
            inde = arr[:p+1].index(maxi) + 1
            while arr[0] != maxi:
                arr[:inde] = arr[:inde][::-1] 
                result.append(inde)
                inde = arr[:inde].index(maxi) + 1

            arr[:p+1] = arr[:p+1][::-1]  
            result.append(p+1)
            p -= 1
        return result