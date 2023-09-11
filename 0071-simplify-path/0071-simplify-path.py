class Solution(object):
    def simplifyPath(self, path):
        lst = []
        strings = path.split("/")
    
        for string in strings:
           if string == "..":
              if lst:
                   lst.pop()
           elif string and string != ".":
              lst.append(string)
    
        return "/" + "/".join(lst)
        