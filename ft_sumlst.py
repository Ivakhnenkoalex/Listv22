def ft_len(str):
    l = 0
    for i in str:
        l += 1
    return (l)


def ft_sumlst(lst):
    d = ft_len(lst)
    i = 0
    r = 0
    while d > i:
        r = r + lst[i]
        i = i + 1
    return r
