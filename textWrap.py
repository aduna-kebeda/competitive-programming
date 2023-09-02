import textwrap

def wrap(string, max_width):
    result=[]
    n=len(string)
    i=0
    while i<n:
        if n-i<=max_width:
            result.append(string[i:n])
            break;
        else:
            result.append(string[i:i+max_width])
            i+=max_width
        
    return "\n".join(result)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
