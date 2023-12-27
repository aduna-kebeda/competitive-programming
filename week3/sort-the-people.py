class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        for i in range(len(heights)):
            j=i
            while j>0:
                if heights[j]>heights[j-1]:
                    heights[j], heights[j-1]=heights[j-1], heights[j]
                    names[j], names[j-1]=names[j-1], names[j]
                else:
                    break
                j-=1
        return names

                    
        
