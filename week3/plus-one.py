from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1 

        for i in range(len(digits) - 1, -1, -1):
            total = digits[i] + carry
            if total == 10:
                carry = 1
                digits[i] = 0
            else:
                carry = 0
                digits[i] = total

       
        if carry > 0:
            digits.insert(0, carry)

        return digits