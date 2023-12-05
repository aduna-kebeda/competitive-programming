class Solution(object):
    def numberOfMatches(self, n):
        count=0
        while n>1:
            if n%2!=0:
                count+=int(n/2)
                n=int(n/2)+1
            else:
                count+=int(n/2)
                n=int(n/2)
        return count

        