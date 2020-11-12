def ft_len(str):
    a = 0
    for i in str:
        a += 1
    return a


def ft_odd_even_analysis_lst(lst):
    d = ft_len(lst)
    i = 0
    k2 = 0
    mx2 = lst[0]
    mn2 = lst[0]
    sum2 = 0
    k1 = 0
    mx1 = lst[1]
    mn1 = lst[1]
    sum1 = 0
    while d > i:
        if lst[i] % 2 == 0:
            k2 = k2 + 1
            if lst[i] > mx2:
                mx2 = lst[i]
            if lst[i] < mn2:
                mn2 = lst[i]
            sum2 = sum2 + lst[i]
            i = i + 1
        else:
            k1 = k1 + 1
            if lst[i] > mx1:
                mx1 = lst[i]
            if lst[i] < mn1:
                mn1 = lst[i]
            sum1 = sum1 + lst[i]
            i = i + 1
    print("Анализ списка:\n"
    "Количество четных чисел:{},\t\tКоличество нечетных чисел:{},\n"
    "Максимальная четная цифра:{},\t\tМаксимальная нечетная цифра:{},\n"
    "Минимальная чентая цифра:{},\t\tМинимальная четная цифра:{},\n"
    "Сумма четных чисел:{},\t\tСумма нечетных чисел:{},"
    "".format(k2,k1,mx2,mx1,mn2,mn1,sum2,sum1))
