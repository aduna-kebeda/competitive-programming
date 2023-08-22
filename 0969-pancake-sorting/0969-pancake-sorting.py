class Solution:
    def pancakeSort(self, arr):
        flips = []
        n = len(arr)
        
        for i in range(n, 0, -1):
            
            maxi = arr.index(i)
            
           
            arr[:maxi + 1] = reversed(arr[:maxi + 1])
            flips.append(maxi + 1)
            
            
            arr[:i] = reversed(arr[:i])
            flips.append(i)
        
        return flips