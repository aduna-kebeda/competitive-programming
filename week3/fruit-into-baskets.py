class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left=0
        maxi=0
        dic={}
        for right in range(len(fruits)):
            if fruits[right] in dic:
               dic[fruits[right]]+=1 
            else:
                dic[fruits[right]]=1 

            if len(dic)>2:
                maxi=max(maxi, right-left) 
                while left<right and len(dic)>2:

                    dic[fruits[left]]-=1
                    if dic[fruits[left]]<=0:
                        dic.pop(fruits[left]) 
                    left+=1 
            maxi=max(maxi, right-left+1)
        return maxi
                
                

