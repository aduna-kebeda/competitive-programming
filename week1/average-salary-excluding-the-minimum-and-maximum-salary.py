class Solution(object):
    def average(self, salary):
        add = sum(salary)
        result = add - max(salary) - min(salary)
        div = len(salary) - 2
        av = float(result) / div 
        return av
