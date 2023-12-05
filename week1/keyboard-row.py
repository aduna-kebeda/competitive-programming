class Solution(object):
    def findWords(self, words):
        store=[]
        for word in words:
            first=word[0].lower()
            if first in "qwertyuiop":
                check=True
                for i in range(len(word)):
                    char=word[i].lower()
                    
                    if char not in "qwertyuiop":
                        check=False
                if check==True:
                    store.append(word)
            elif first in "asdfghjkl":
                check=True
                for i in range(len(word)):
                    char=word[i].lower()
                    if char not in "asdfghjkl":
                        check=False
                if check==True:
                    store.append(word)
            elif first in "zxcvbnm":
                check=True
                for i in range(len(word)):
                    char=word[i].lower()
                    if char not in "zxcvbnm":
                        check=False
                if check==True:
                    store.append(word)
        return store
            


        