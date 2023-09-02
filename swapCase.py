def swap_case(s):
    output=""
    for i in range(len(s)):
        if s[i].isupper():
            output+=s[i].lower()
        elif s[i].islower():
            output+=s[i].upper()
        else:
            output+=s[i]
    return output

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
