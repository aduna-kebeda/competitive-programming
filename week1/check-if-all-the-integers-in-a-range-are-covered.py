class Solution(object):
    def isCovered(self, ranges, left, right):
        s=set()
        for i in range(len(ranges)):
           st=ranges[i][0]
           e=ranges[i][1]
           for j in range(st, e+1):
               s.add(j)
        print(s)
        if left in s and right in s:
            for j in range(left, right):
                if j not in s:
                    return False
        else:
            return False
        return True
            
       