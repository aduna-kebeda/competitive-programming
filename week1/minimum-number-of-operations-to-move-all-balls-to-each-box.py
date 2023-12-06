class Solution(object):
    def minOperations(self, boxes):
        result=[]
        for i in range(len(boxes)):
            add=0
            
            for j in range(len(boxes)):
                if boxes[j]=='1':
                    add+=abs(j-i)
            result.append(add)
        return result