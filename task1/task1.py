n, m = map(int, input().split())

lst_n = [i for i in range(1, n+1)]

tmp = lst_n[0]
tmp1 = 0

i = 0
t = m
lst_it = []
while tmp != tmp1:
    lst_tmp = lst_n[i:t]
    if len(lst_tmp) < m:
        lst_tmp1 = lst_n
        lst_n += lst_tmp1
        continue

    lst_it.append(lst_tmp[0])
    i += (m - 1)
    t += (m - 1)
    tmp1 = lst_tmp[-1]

print(''.join(map(str, lst_it)))