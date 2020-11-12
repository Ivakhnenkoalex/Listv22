def ft_len(a):
    b = 0
    for i in a:
        b += 1

    return b


def ft_rmstrspc(str):
    d = ft_len(str)
    i = 0
    r = ''
    while d > i:
        if str[i] == ' ':
            i = i + 1
        else:
            r = r + str[i]
            i = i + 1
    return r
