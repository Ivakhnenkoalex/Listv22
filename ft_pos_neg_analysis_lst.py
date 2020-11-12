def ft_len(str):
    c = 0
    for i in str:
        c += 1
    return c


def ft_pos_neg_analysis_lst(lst):
    d = ft_len(lst)
    lst1 = []
    lst0 = []
    mx1 = -999999999
    mn1 = 999999999
    sum1 = 0
    sum2 = 0
    sr1 = 0
    mn2 = 999999999
    mx2 = -9999999
    ko = 0
    sr2 = 0
    k1 = 0
    k2 = 0
    c = d
    i = 0
    while d > i:
        if lst[i] == 0:
            ko = ko + 1
            i = i + 1
        if lst[i] > 0:
            lst1.append(lst[i])
            k2 = k2 + 1
            if lst[i] > mx1:
                mx1 = lst[i]
            if lst[i] < mn1:
                mn1 = lst[i]
            sum1 = sum1 + lst[i]
            i = i + 1
        if lst[i] < 0:
            lst0.append(lst[i])
            k1 = k1 + 1
            if lst[i] > mx2:
                mx2 = lst[i]
            if lst[i] < mn2:
                mn2 = lst[i]
            sum2 = sum2 + lst[i]
            i = i + 1
    sr1 = sum1 / k2
    sr2 = sum2 / k1
    print("Положительные:{}\tОтрицательные:{}\n"
          "Количество чисел:{},\tКоличество чисел:{},\n"
          "Максимальная цифра:{},\tМаксимальная цифра:{},\n"
          "Минимальная цифра:{},\tМинимальная цифра:{},\n"
          "Сумма цифр:{},\tСумма цифр:{},\n"
          "Среднее значение:{}\tСреднее значение:{}\n"
          ""
          "Количество нулей:{}".format(lst1, lst0, k2, k1, mx1, mx2, mn1, mn2, sum1, sum2, sr1, sr2, ko))
