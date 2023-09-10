n = int(input())
a = list(map(int, input().split()))

odd = False
even = False

for num in a:
    if num % 2 == 0:
        even = True
    else:
        odd = True

if odd and even:
    a.sort()

for num in a:
    print(num, end=' ')
