class Solution:
    def smallestNumber(self, num: int) -> int:
        lst=[]
        digit=abs(num)
        if num==0:
            return 0
        while digit>0:
            lst.append(digit%10)
            digit=digit//10
        lst.sort()
        print(lst)
        if num<0:
            r=[str(lst[i]) for i in range(len(lst)-1, -1, -1)]
           
            return int('-'+''.join(r))
        else:
            
            i=0
            while i<len(lst):
                i+=1
                if lst[i]!=0:
                    break 
            if lst[0]==0:
               lst[0], lst[i]=lst[i], lst[0]
            r=[str(d) for d in lst]
            return int(''.join(r))

        
     
        