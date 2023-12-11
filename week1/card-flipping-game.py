class Solution(object):
    def flipgame(self, fronts, backs):
        both=[fronts[i] for i in range(len(fronts)) if fronts[i]==backs[i]]
        
        num=float('inf')
        for i in range(len(fronts)):
            if fronts[i] not in both:
                if fronts[i]<num:
                    num=fronts[i]
            if backs[i] not in both:
                if backs[i]<num:
                    num=backs[i]

        if num in fronts or num in backs:
            return num
        else:
             return 0 