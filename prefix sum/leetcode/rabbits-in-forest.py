class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        dic = defaultdict(int)
        cnt = 0

        for i in range(len(answers)):
            if answers[i] == 0:
                cnt += 1
            elif dic[answers[i]] == 0 or dic[answers[i]] % (answers[i] + 1) == 0:
                cnt += answers[i] + 1
            dic[answers[i]] += 1

        return cnt
