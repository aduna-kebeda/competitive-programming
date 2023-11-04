class Solution(object):
    def plusOne(self, digits):
        string = ""
        lst = []
        for i in range(len(digits)):
            string += str(digits[i])
        num = int(string)
        num += 1
        num = str(num)
        for i in range(len(num)):
            lst.append(num[i])

        return [int(x) for x in lst]