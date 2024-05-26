if __name__ == '__main__':
    x = [1, 2, 3]
    z = [1, 2, 3]
    a = 7
    b = 7
    m = [0]*3
    m[1]=1
    # print(id(x))
    # y = x
    # print(id(y))
    # print(id(z))
    # print(id(a))
    # print(id(b))
    print(id(x[0]))
    print(id(x[1]))
    print(id(x[2]))
    # print(id(x[3]))
    print(id(m[0]))
    print(id(m[1]))

