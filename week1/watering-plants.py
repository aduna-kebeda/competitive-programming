class Solution(object):
    def wateringPlants(self, plants, capacity):
        c=0
        cap=capacity
        i=0
        while i<(len(plants)):
            if cap>=plants[i]:
                cap-=plants[i]
                c+=1
                
            else:
                c+=i+i
                cap=capacity
                print(c)
                continue
                
            i+=1
        return c
        