class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        result=[]
        maxi=max(candies)
        for i in range(len(candies)):
            if maxi-(candies[i]+extraCandies)>0:
                result.append(False)
            else:
                result.append(True)
        return result
        