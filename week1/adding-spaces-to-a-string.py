class Solution(object):
    def addSpaces(self, s, spaces):
        substrings = []
      
        substrings.append(s[:spaces[0]])
        
        for i in range(1, len(spaces)):
            prev, now = spaces[i - 1], spaces[i]
            substrings.append(' ' + s[prev:now])

        substrings.append(' ' + s[spaces[-1]:] if spaces else '')

        result = ''.join(substrings)
        return result
