#Bài 1: Viết hàm có hai tham số là chiều dài và chiều rộng hình chữ 
#nhật để tính và xuất ra màn hình chu vi và diện tích của hình. Nhập 
#vào chiều dài, chiều rộng rồi gọi hàm trên.

def bai1(a, b):
    dt = a*b
    cv = (a+b)*2
    return dt, cv

dai = float(input("Nhập chiều dài: "))
rong = float(input("Nhập chiều rộng: "))
dt, cv = bai1(dai,rong)
print(f"Chu vi HCN: {dt}")
print(f"Diện tích HCN: {cv}")

#Bài 2: Viết hàm kiểm tra một số có là số nguyên tố không. Nhập vào 
#số nguyên dương rồi gọi hàm trên để thông báo kết quả kiểm tra.

# Nâng cao
def bai2(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1)) #all trả về true false

# Cơ bản
def bai2_Basic(n):
    if n >= 1:
        if n == 1: return True
        else: 
            for i in range(2, int(n**0.5 + 1)):
                if n % i == 0: 
                    return False
    return True
n = int(input("Nhập số cần kiểm tra: "))
print(bai2(n))
print(bai2_Basic(n))

#Bài 3: Viết hàm tính tổng hai số a, b. Nhập vào a, b rồi gọi hàm trên
#để in ra tổng.
def bai3(a, b):
    dt = a+b
    return dt

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
print(f"Tổng a, b là {bai3(a,b)}")

#Bài 4: Viết hàm tính tích các số từ 1 đến n. Nhập vào n rồi gọi hàm 
#trên để in ra tổng.

def list42(b):
    return sum(b)

n = int(input("Nhập số phần tử: "))
list4 = []
for i in range(0, n):
    list4.append(float(input(f"Nhập giá trị A{i+1}: ")))
print(f"Sum(A) = {list42(list4)}")

#Bài 5: Viết hàm đếm số từ có trong một chuỗi. Nhập vào một chuỗi 
#rồi gọi hàm trên.

def list55(b):
    c = [len(i) for i in b]
    return c

n = int(input("Nhập số phần tử: "))
list5 = []
for i in range(0, n):
    list5.append(input(f"Nhập giá trị A{i+1}: "))
b = list55(list5)
print(f"Số kí tự mỗi phần tử = {b}")

#Bài 6: Viết hàm thay từ “tin học” bằng “CNTT” trong một chuỗi. Nhập 
#vào một chuỗi rồi gọi hàm trên để in ra kết quả

def thay_the_chuoi(chuoi):
    return chuoi.replace("tin học", "CNTT")

chuoi_input = input("Nhập chuỗi: ")

print(thay_the_chuoi(chuoi_input))

