class Solution(object):
    def findDiagonalOrder(self, matrix):
       
        dic={}
		
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
				
                if i + j not in dic:
                    dic[i+j] = [matrix[i][j]]
                else:
                    dic[i+j].append(matrix[i][j])
        ans= []
		
        for key, value in dic.items():
            if key % 2 == 0:
                [ans.append(x) for x in value[::-1]]
            else:
                [ans.append(x) for x in value]
        return ans
                
            
				
