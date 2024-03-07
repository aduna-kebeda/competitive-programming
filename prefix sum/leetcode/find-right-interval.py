class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # if len(intervals)<2:
        #     return [-1]
        dic=defaultdict(int)
        next=[]
        for i in range(len(intervals)):
            dic[intervals[i][0]]=i
            next.append(intervals[i][0])
        next.sort()
        result=[]
        for i in range(len(intervals)):
            left = 0
            right = len(intervals) - 1
            ans=-1
            while left <= right:
                mid = (left + right)//2
                ans=mid
                if next[mid] < intervals[i][1]:
                    left = mid + 1
                elif next[mid] > intervals[i][1]:
                    right = mid - 1
                else:
                    break
            
            if next[-1] >= intervals[i][1]:
               if next[ans] < intervals[i][1]:
                   result.append(dic[next[ans+1]])
               else:
                   result.append(dic[next[ans]])
               

            else:
                result.append(-1)

       
        return result