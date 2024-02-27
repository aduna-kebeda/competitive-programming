class Solution:
    def countGoodNumbers(self, a: int) -> int:
        
        def divide(base, n):
            if n==0:
                return 1
            if n==1:
                return base
            ans=divide(base, floor(n/2))
            if n%2==0:
                return (ans*ans)%(10**9 + 7)
            else:
                return (ans*ans*base)%(10**9 + 7)
        
        return (divide(5, ceil(a/2))*divide(4, floor(a/2) ))%(10**9 + 7)
