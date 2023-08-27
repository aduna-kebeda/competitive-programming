class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        c=0
        s=0
        while s<len(people):
            if people[s]>limit:
                break
            else:    
                s=s+1
        left=0
        right=s-1
        while left<=right:
            if people[left]+people[right]<=limit:
                left=left+1
                right=right-1
            else:
                right=right-1

            c=c+1
            




        return c
        