class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        def solve(left, right, turn):
            if left == right:
                if turn:
                    return [nums[left], 0]
                else:
                    return [0, nums[left]]
            
            leftScore = solve(left + 1, right, not turn)
            rightScore = solve(left, right - 1, not turn)

            if turn:
                leftScore[0] += nums[left]
                rightScore[0] += nums[right]

                return leftScore if leftScore[0] > rightScore[0] else rightScore
            else:
                leftScore[1] += nums[left]
                rightScore[1] += nums[right]

                return leftScore if leftScore[1] > rightScore[1] else rightScore

        result = solve(0, len(nums) - 1, True)
        return result[0] >= result[1]
