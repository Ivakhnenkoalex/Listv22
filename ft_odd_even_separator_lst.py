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
    rk = [[0],[0]]
    while d > i:
        if lst[i] % 2 == 0:
            r1.append(lst[i])
        elif lst[i] % 2 != 0:
            r2.append(lst[i])
        i = i + 1
    rk[0] = r2
    rk[1] = r1
    return rk
