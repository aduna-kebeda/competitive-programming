class Solution(object):
    def findSpecialInteger(self, arr):
        count={}
        maxi=0
        repeat=arr[0]
        for num in arr:
            count[num]=count.get(num, 0)+1
            if count[num]>maxi:
                maxi=count[num]
                repeat=num
        return repeat
        
        