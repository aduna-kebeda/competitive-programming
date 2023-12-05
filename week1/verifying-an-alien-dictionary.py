class Solution(object):
    def isAlienSorted(self, words, order):
       
       for i in range(1, len(words)):
           word2=words[i]
           word1=words[i-1]
           mini=min(len(word1), len(word2))
           j=0
           while j<(mini):
               if order.index(word2[j])<order.index(word1[j]):
                   return False
               elif order.index(word2[j])>order.index(word1[j]):
                   break
               j+=1
           if j==mini:
               if len(word1)>len(word2):
                   return False

            
       return True

           


        