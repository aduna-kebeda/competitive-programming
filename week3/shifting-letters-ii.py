class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        pre=[0]*len(s)
        for shift in shifts:
            if shift[2]==1:
               pre[shift[0]]+=1
               if shift[1]!=len(s)-1:
                   pre[shift[1]+1]-=1
            else:
                pre[shift[0]]-=1
                if shift[1]!=len(s)-1:
                   pre[shift[1]+1]+=1
        add=0  
        print(pre)
        for i in range(len(s)):
            add+=pre[i]
            pre[i]=add
        print(pre)
        arr=['']*len(s)
        for i in range(len(s)):
            char=ord(s[i])-ord('a')+pre[i]
            char=char%26 +ord('a')

            char=chr(char)
            arr[i]=char
            

      
        return ''.join(arr)
            



        
