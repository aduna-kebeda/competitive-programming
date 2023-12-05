class Solution(object):
    def escapeGhosts(self, ghosts, target):
        
        for i in range(len(ghosts)):
            mine=abs(target[0]-0)+abs(target[1]-0)
            ghost = abs(target[0] - ghosts[i][0]) + abs(target[1] - ghosts[i][1])

            if ghost<=mine:
                return False
        return True
        