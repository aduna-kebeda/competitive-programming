class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
       cnt=Counter(s1)
       for i in range(len(s2)-len(s1)+1):
           check=Counter(s2[i:i+len(s1)])
           
           for j in range(len(s1)):
               if cnt[s1[j]]!=check[s1[j]]:
                   break

           else:
               return True
       return False