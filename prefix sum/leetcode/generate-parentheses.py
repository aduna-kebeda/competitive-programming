class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def backTrack(string, open, close):
            if open==n and open==close:
                if "".join(string) not in result:
                    result.add("".join(string))
                return 
           

            if open<n:
                string.append('(')
                open+=1
                backTrack(string, open, close)
                open-=1
                string.pop()
            if close<open:
                string.append(')')
                close+=1
                backTrack(string, open, close)
                close-=1
                string.pop()

        
        result=set()
        backTrack([], 0, 0)
        return result

