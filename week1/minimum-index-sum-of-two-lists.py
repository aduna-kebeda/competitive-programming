class Solution(object):
    def findRestaurant(self, list1, list2):
        maxi=max(len(list1), len(list2))
        lon=list1[:]
        if len(list1)<len(list2):
            lon=list2[:]
        string=""
        mini=float('inf')
        arr=[]
        for i in range(maxi):
           
            if lon[i] in list1 and lon[i] in list2 :
                a=list1.index(lon[i])
                b=list2.index(lon[i])
                if a+b<mini:
                    arr=[]
                    arr.append(lon[i])
                    mini=a+b
                elif a+b==mini:
                    arr.append(lon[i])
        
        
        return arr