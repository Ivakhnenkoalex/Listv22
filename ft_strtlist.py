def ft_len_mass(mass):
    a = 0
    for i in mass:
        a += 1
    return a


def ft_strtlist(str):
    d = ft_len_mass(str)
    i = 0
    l = []
    while d > i:
        l.append(str[i])
        i = i + 1
    return l
