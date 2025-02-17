# Bài 1: Phân tích ma trận
# Viết một chương trình thực hiện các thao tác sau:
# Tạo một ma trận ngẫu nhiên kích thước 𝑚×𝑛 (người dùng nhập giá trị  𝑚 và 𝑛 từ bàn phím).
# Tìm giá trị lớn nhất và nhỏ nhất trong ma trận.
# Tính tổng các phần tử trên từng hàng và từng cột.
# Tìm chỉ số (index) của phần tử lớn nhất trong toàn bộ ma trận.
# Gợi ý:
# Dùng numpy.random.randint() để tạo ma trận.
# Sử dụng các hàm như numpy.max(), numpy.min(), numpy.sum().

import numpy as np

m = int(input())
n = int(input())

arr = np.random.randint(1, 100, (m, n))
print(arr)

print("Max:", np.max(arr))
print("Min:", np.min(arr))

print("Sum of rows:", np.sum(arr, axis=1))
print("Sum of columns:", np.sum(arr, axis=0))

max_index = np.unravel_index(np.argmax(arr), arr.shape)
print("Index of max element:", max_index)
