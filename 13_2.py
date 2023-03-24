s = 'АБ БД ВА ГБВЕ ДЖ ЕВК ЖГ ЗЖД КЗ'
d = {i[0]: i[1:] for i in s.split()}


def f(s, e):
    if s.count(s[-1]) == 2 and len(s) > 1:
        return 1
    return sum(f(s + c, e) for c in d[s[-1]])


print(f("Е", "Е"))