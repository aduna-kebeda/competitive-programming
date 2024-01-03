class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        cnt=0
        cnt2=0
        skill.sort()
        left=0
        right=len(skill)-1
        check=skill[0] + skill[len(skill)-1]
        while left<right:
            cnt+=skill[left]*skill[right]
            cnt2=skill[left] + skill[right]
            if cnt2!=check:
                print(cnt2)
                return -1
            left+=1
            right-=1

        return cnt
            