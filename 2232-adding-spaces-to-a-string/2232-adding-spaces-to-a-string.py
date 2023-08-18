class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
       
        control = 0
        for i in range(len(spaces)):
            l = spaces[i]
            s = s[0:l+control] + " " + s[l+control:]
            control = control + 1
        return s