d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sv = sorted(d.values())
sd = {}
for i in sv:
    for k in d.keys():
        if d[k] == i:
            sd[k] = d[k]
            break
print('Сортировка по возрастанию', sd)
sv = sorted(d.values(), reverse=True)
sd = {}
for i in sv:
    for k in d.keys():
        if d[k] == i:
            sd[k] = d[k]
            break
print('Сортировка по убыванию', sd)