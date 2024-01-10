class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left=0 
        W=0
        
        while left<k:
            if blocks[left]=='W':
                W+=1
            left+=1
        mini=W
        for right in range(left, len(blocks)):
            if blocks[right]=='W':
                W+=1
            if blocks[right-k]=='W':
                W-=1
            mini=min(mini, W)
        return mini
            
                

