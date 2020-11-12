def ft_len_mass(mass):
    a = 0
    for i in mass:
        a += 1
    return a


def ft_join(lst, s =' '):
    d = ft_len_mass(lst)
    i = 0
    r = ''
    while d > i:
        if lst[i] == 0:
            r = r + '0'
        elif lst[i] == 1:
            r = r + '1'
        elif lst[i] == 2:
            r = r + '2'
        elif lst[i] == 3:
            r = r + '3'
        elif lst[i] == 4:
            r = r + '4'
        elif lst[i] == 5:
            r = r + '5'
        elif lst[i] == 6:
            r = r + '6'
        elif lst[i] == 7:
            r = r + '7'
        elif lst[i] == 8:
            r = r + '8'
        elif lst[i] == 9:
            r = r + '9'
        else:
            r = r + lst[i]
        if i != d - 1:
            r = r + s
        i = i + 1
    return r
