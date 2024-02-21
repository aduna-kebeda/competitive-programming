class Solution:
    def numberOfWays(self, s: str) -> int:
      pre0=[0]*(len(s)+1)

      zero=0
      for i in range(len(s)):
          if s[i]=="1":
              pre0[i]=zero
          else:
            zero+=1
      pre1=[0]*(len(s)+1)
      
      one=0
      for i in range(len(s)):
          if s[i]=="0":
              pre1[i]=one
          else:
            one+=1
      
    
      cnt0=0
      cnt1=0
      a=0
      b=0
      for i in range(len(s)):
          if s[i]=='0':
              a+=cnt0
          cnt0+=pre0[i]
      for i in range(len(s)):
          if s[i]=='1':
              b+=cnt1
          cnt1+=pre1[i]

      return a+b
          