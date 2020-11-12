def ft_len(a):
    b = 0
    for i in a:
        b += 1

    return b


def ft_rmstrchar(str, less):
    d = ft_len(str)
    k = ft_len(less)
    i = 0
    w = 0
    r = ''
    while k > w and d > i:
        if str[i] == less[w]:
            i = i + 1
            w = 0
        elif str[i] != less[w] and w == k - 1:
            r = r + str[i]
            i = i + 1
            w = 0
        else:
            w = w + 1
    return r
