class Solution:
    def myPow(self, x: float, n: int) -> float:

        def power(x, n):
            if n==0:
                return 1
            if n==1:
                return x
            
            ans=power(x, floor(n/2))
            if n%2==0:
                return ans*ans
            else:
                return ans*ans*x
            return ans
        ans=power(x, abs(n))
        return  ans if n>=0 else 1/ans  