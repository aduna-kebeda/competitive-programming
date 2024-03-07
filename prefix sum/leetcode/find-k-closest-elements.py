class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0 
        right = len(arr)-1
        ans=-1
        while left <= right:
            mid=(left + right)//2
            
            if arr[mid] >= x:
                right = mid - 1
            elif arr[mid] < x:
                ans=mid
                left = mid + 1
            # else:
            #     left=mid
            #     break
      
        result=[]
        
        right=left 
        left -= 1   
        for i in range(k):
            if  (right >= len(arr)) or (left > -1 and abs(arr[left] - x) <= abs(arr[right] - x)):
                result.append(arr[left])
                left -= 1
            elif right < len(arr):
                result.append(arr[right])
                right += 1
        result.sort()
        return result


        
        