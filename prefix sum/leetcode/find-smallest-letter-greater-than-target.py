class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left=0
        right=len(letters)-1
        while left <= right:
            mid=(left + right)//2
            print(mid)
            if ord(letters[mid]) > ord(target):
                right = mid - 1
            else:
                left = mid + 1
        
           
        if right < 0 or  left > len(letters)-1:
            return letters[0]
        return letters[left]