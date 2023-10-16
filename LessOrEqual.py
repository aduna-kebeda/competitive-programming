n, m = map(int, input().split())
a = [1] + [int(x) for x in input().split()] + [1000000001]
a.sort()
 
if a[m] == a[m + 1]:
    print("-1")
else:
    print(a[m])
