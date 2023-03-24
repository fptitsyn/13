s = "АГ БА ВБГ ГВД ДАБВ"
d = {i[0]: i[1:] for i in s.split()}


def f(s, e):
    if s[0] == s[-1] and len(s) > 1:
        return 1
    return sum(f(s + c, e) for c in d[s[-1]] if s.count(c) <= 1)


print(f("А", "А"))