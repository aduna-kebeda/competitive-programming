class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic={'2': "abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        
        def backTrack(idx, sub):
            if len(sub)==len(digits):
                if not sub:
                    return 
                result.append(''.join(sub[:]))
                return 
            if idx > len(digits):
                return
            for i in range(idx,len(digits)):
                string=dic[digits[i]]
                for j in range(len(string)):
                    sub.append(string[j])
                    
                    backTrack(i+1, sub)
                    sub.pop()

        result=[]
        backTrack(0, [])
        return result

        