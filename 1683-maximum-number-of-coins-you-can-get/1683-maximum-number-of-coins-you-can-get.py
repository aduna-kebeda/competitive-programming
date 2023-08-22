class Solution(object):
    def maxCoins(self, piles):
    
            
        piles.sort(reverse=True)

        total = 0
        n = len(piles)/3
        i = 1 

        for s in range(n):
                total += piles[i]
                i += 2 

        return total