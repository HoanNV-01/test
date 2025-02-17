a = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 10, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 55, 24, 25],
    [22, 27, 35, 30, 29]
    ]
test = []
for i in a:
    i.sort()
    n = i[0]
    c = False
    for j in i:
        if(j != n):
            test.append(False)
            c = True
            break
        else: n += 1
    if(c != True): test.append(i)
t1 = t2 = vt = 0
for k in test:
    if(k != False):
        t2 = k[len(k)-1]
        if t2 > t1: t1 = t2
    vt += 1
print(f"Số lớn nhất là: {t1}")
print(f"Vị trí mảng có giá trị lớn nhất là: {vt-1}")


