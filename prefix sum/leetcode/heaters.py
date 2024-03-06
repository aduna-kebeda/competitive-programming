class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        # maxi=0
        # for i in range(len(houses)):
        #     mini=inf
        #     for heat in heaters:
        #         mini=min(mini, abs(heat - houses[i]))
        #     maxi=max(maxi, mini)
        # return maxi 

        heaters.sort()
        houses.sort()
        maxi=0
        for i in range(len(houses)):
            
            left=0
            right=len(heaters)-1
            mid = (left + right)//2
            mini=float('inf')
            while left <= right:
                mid = (left + right)//2
                if heaters[mid] > houses[i]:
                    mini=min(mini, abs(heaters[mid] - houses[i]))
                    right = mid -1
                else:
                    mini=min(mini, abs(heaters[mid] - houses[i]))
                    left = mid + 1
                
            maxi= max(maxi, mini)

        return maxi