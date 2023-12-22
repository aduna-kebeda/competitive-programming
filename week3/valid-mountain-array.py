class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        maxi = max(arr)
        if arr.count(maxi) > 1 or len(arr) < 3:
            return False
        else:
            left = 0
            right = len(arr) - 1
            
            while left < right:
                if arr[left + 1] == maxi and arr[right - 1] == maxi:
                    print(left, right)
                    return True
              
                if arr[left] >= arr[left + 1] or arr[right] >= arr[right - 1]:
                    return False
                
                if arr[right - 1] != maxi:
                   
                    right -= 1
                    
                if arr[left + 1] != maxi:
                    left += 1
                
            return True
