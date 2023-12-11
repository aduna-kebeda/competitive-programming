class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        evenSum=sum([num for num in nums if num%2==0])
        result=[]
        for querie in queries:
            
            if nums[querie[1]]%2==0:
                if querie[0]%2==0:
                    evenSum+=querie[0]
                    result.append(evenSum)
                   
                else:
                    evenSum-=nums[querie[1]]
                    result.append(evenSum)
            else:
                if querie[0]%2==1:
                    evenSum+=querie[0] +nums[querie[1]]
                    result.append(evenSum)
                else:
                    result.append(evenSum)
            nums[querie[1]]+=querie[0]

        return result
        