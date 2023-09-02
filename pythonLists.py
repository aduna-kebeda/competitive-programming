if __name__ == '__main__':
    N = int(input())
    lst = []

    for _ in range(N):
        command = input().split()
        op = command[0]

        if op == "insert":
            index = int(command[1])
            element = int(command[2])
            lst.insert(index, element)
        elif op == "print":
            print(lst)
        elif op == "remove":
            element = int(command[1])
            lst.remove(element)
        elif op == "append":
            element = int(command[1])
            lst.append(element)
        elif op == "sort":
            lst.sort()
        elif op == "pop":
            lst.pop()
        elif op == "reverse":
            lst.reverse()
