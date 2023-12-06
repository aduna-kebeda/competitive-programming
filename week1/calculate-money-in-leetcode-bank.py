class Solution(object):
    def totalMoney(self, n):
        result=0
        count=1
        check=1
        for i in range((n)):
            result+=count
            if count==check+6:
                check+=1
                count=check
                print(check)
            
            else:
                count+=1
        return result
        