class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        p1=0
        p2=0
        string=""
        if name[0]!=typed[0]:
            return False
        while p1<len(name) and p2<len(typed):

            if name[p1]==typed[p2]:
                string+=typed[p2]
                p1+=1
                p2+=1
            elif typed[p2-1]==typed[p2]:
                p2+=1
            else:
                return False
        print(p2)
        if p2<len(typed):
            if len(set(typed[p2:]))==1 and typed[p2-1]==typed[p2]: 
               return name==string
            else:
                return False

        return name==string