class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        sum1=0
        sum2=0
        if destination>start:
           sum1=sum(distance[start:destination])
           sum2=sum(distance)-sum1
        else:
            sum1=sum(distance[destination:start])
            sum2=sum(distance)-sum1
        return min(sum1, sum2)
        