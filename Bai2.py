#Bài 5: Tìm mảng con dài nhất với các số liên tiếp:
# Hàm: longestConsecutiveSubarray
# Input: [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13]
# Output: [5, 6, 7, 8, 9, 10]
lst = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13]
tacharr = []
tam = []
n = lst[0]
for i in lst:
    if i == n:
        tam.append(i)
    else:
        tacharr.append(tam)
        tam = [i]
    n = i + 1
tacharr.append(tam)  
j1 = n = k = 0
for j in tacharr:
    if len(j) > n:
        n = len(j)
        k = j1
    j1 += 1
print(tacharr[k])



