def no_dups(s):
    sl = s.split(' ')
    d = {}
    arr = []
    for i in sl:
        if i not in d:
            d[i] = True
    
    for k, v in d.items():
        arr.append(k)

    return " ".join(arr)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))