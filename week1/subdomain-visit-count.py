class Solution(object):
    def subdomainVisits(self, cpdomains):
        count={}
        result=[]
        for domain in cpdomains:
            num, subdomain=domain.split()
            sub=subdomain.split('.')
            temp=""
            for j in range(len(sub)-1, -1, -1):
                temp=sub[j] + '.' + temp
                count[temp]=count.get(temp, 0)+int(num)
      
        for string , value in count.items():
            temp3=str(value) + " " + string
            if temp3[len(temp3)-1]== '.':
                temp3=temp3[:len(temp3)-1]
            result.append(temp3)
        return result
            

        

        

        
        