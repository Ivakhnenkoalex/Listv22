def ft_len_mass(mass):
    a = 0
    for i in mass:
        a += 1
    return a


def ft_join(lst, s=' '):
    d = ft_len_mass(lst)
    i = 0
    r = ''
    while d > i:
        r = r + lst[i]
        if i != d - 1:
            r = r + s
        i = i + 1
    return r
