class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
       walls=set([(i[0],i[1]) for i in walls ])
       guards=set([(i[0],i[1]) for i in guards ])
       
       check=set()
       for i in range(m):
           for j in range(n):
               if (i ,j) in guards:
                    k=i
                    r=j
                    while r>-1:
                        if (k, r) in walls:
                            break
                        check.add((k,r))
                        r-=1
                        if (k, r) in guards:
                            break
                    k=i
                    r=j
                    while k>-1:
                        if (k, r) in walls:
                            break
                        check.add((k,r))
                        k-=1
                        if (k, r) in guards:
                            break
                    k=i
                    r=j
                    while r<n:
                        if (k, r) in walls:
                            break
                        check.add((k,r))
                        r+=1
                        if (k, r) in guards:
                            break
                    k=i
                    r=j
                    while k<m:
                        if (k, r) in walls:
                            break
                        check.add((k,r))
                        k+=1 
                        if (k, r) in guards:
                            break
                    
      
       return (m*n)-len(check)-len(walls)
                   