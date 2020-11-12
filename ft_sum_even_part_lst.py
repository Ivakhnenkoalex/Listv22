def ft_len(str):
    l = 0
    for i in str:
        l += 1
    return (l)


def ft_sum_even_lst(lst):
    d = ft_len(lst)
    i = 0
    r = 0
    while d > i:
        if lst[i] % 2 == 0:
            r = r + lst[i]
        i = i + 1
    return r
