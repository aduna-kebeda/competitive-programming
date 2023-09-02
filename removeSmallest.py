t = int(input())

for _ in range(t):
    n = int(input())
    lst= list(map(int, input().split()))

    lst.sort()
    bl = True
    for i in range(1, n):
        if lst[i] > lst[i - 1] + 1:
            print("NO")
            bl = False
            break

    if bl:
        print("YES")
