def ft_len(str):
    a = 0
    for i in str:
        a += 1
    return a


def ft_odd_even_separator_lst(lst):
    d = ft_len(lst)
    i = 0
    r1 = []
    r2 = []
    r3 = []
    rk = [[0],[0]]
    while d > i:
        if lst[i] > 0:
            r1.append(lst[i])
        elif lst[i] < 0:
            r3.append(lst[i])
        else:
            r2.append(lst[i])
        i = i + 1
    rk[0] = r3
    rk[1] = r2
    rk[2] = r1
    return rk
