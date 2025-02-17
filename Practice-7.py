#Bài 1: tính tổng của các phần tử trong một list sau: _list= [1, 2, 3, 4, 5, 6, 7, 8, 9].

# Nâng cao
_list= [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Tổng các phần tử trong {_list} : {sum(_list)}")
# Cơ bản
Tong = 0
for i in _list:
    Tong += i
print(f"Tổng các phần tử trong {_list} : {Tong}")

#Bài 2: Tính tích của các phần tử trong một list sau: _list2 = [1, 2, 3, 4, 5].

# Nâng cao
_list2 = [1, 2, 3, 4, 5]
import math as ma
print(f"Tổng các phần tử trong {_list2} : {ma.prod(_list2)}")
# Cơ bản
Tich = 1 # Nếu tích bằng 0 thì nhân các phần tử đều = 0
for i2 in _list2:
    Tich *= i2
print(f"Tổng các phần tử trong {_list2} : {Tich}")

#Bài 3: Cho _list= [1, 2, 3, 4, 5, 6, 7, 8, 9]. 
#       Tạo 2 list mới từ list gồm 1 list chỉ bao gồm số chẵn (even), 1 list chỉ bao gồm số lẻ (odd).

_list3= [1, 2, 3, 4, 5, 6, 7, 8, 9]
_list_even, _list_odd = [],[] #even: chẵn, odd: lẻ
for i3 in _list3:
    if(i3%2==0):
        _list_even += str(i3)
    else: _list_odd += str(i3)
print(f"Even: [{_list_even}]")
print(f"Odd: [{_list_odd}]")

#Bài 4: Cho _list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']. 
#Tạo danh sách mới chứa 2 phần tử ở vị trí thứ 2 và thứ 3 _new = ['White', 'Black']

_list4 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
_list4_new = _list4[2], _list4[3]
print(_list4_new)

#Bài 5: Cho danh sách đầu vào _list = [‘zero’, ‘three’]. 
#Tạo ra danh sách mới _new = [‘zero’, ‘one’, ‘two’, ‘three’] bằng cách thêm các phần tử vào danh sách ban đầu.

_list5 = ["zero", "three"]
full_list5 = ['zero', 'one', 'two', 'three']
_new_list5 = []
for item in full_list5:
    if item in _list5:
        _new_list5.append(item)
    else:
        _new_list5.append(item)
_list5.clear()
_list5 = _new_list5
print(_list5)

#Bài 12: Đếm số phần tử trong mảng có tổng số kí tự khác nhau (Tự chế)

list12 = ['abc', 'xyz', 'aba', '1221', 'ii', 'ii2', '5yhy5']
dem = 0
lenstr = [len(i6) for i6 in list12]
lenstr_test = []
for i12 in list12:
    if ((len(i12) in lenstr) and (len(i12) not in lenstr_test)):
        lenstr_test.append(len(i12))
        dem += 1
print(dem)
print(lenstr_test)

#Bài 6: Đếm số chuỗi thỏa mãn điều kiện ký tự đầu tiên và cuối cùng là giống nhau từ một danh sách cho trước. 
#Ví dụ cho list = ['abc', 'xyz', 'aba', '1221', ‘ii’, ‘ii2’, ‘5yhy5’] → Kết quả cho ra 4 (đã sửa đầu bài)

list6 = ['abc', 'xyz', 'aba', '1221', 'ii', 'ii2', '5yhy5']
dem = 0
for i6 in list6:
    if(i6[0] == i6[-1]):
        dem += 1
print(dem)

#Bài 7: tạo một list mới bằng cách loại bỏ các phần tử có giá trị giống nhau trong list. 
#Ví dụ: cho _list= ['abc', 'xyz', 'abc', '12', ‘ii’, ‘12’, ‘5a’] → kết quả list mới là _new= ['xyz',‘ii’,‘5a’]

_list7= ['abc', 'xyz', 'abc', '12', 'ii', '12', '5a']
_list7_test = []
for i7 in _list7:
    if _list7.count(i7) < 2:
        _list7_test.append(i7)
print(_list7_test)

#Bài 8: lấy ra số lớn nhất trong list: _list= [11, 2, 23, 45, 6, 9].
#Cơ bản
_list8 = [11, 2, 23, 45, 6, 9]
max1 = _list8[0]
for i8 in range(0, len(_list8)):
    if(_list8[i8] >= max1):
        max1 = _list8[i8]
print(max1)
#Nâng cao
print(max(_list8))

#Bài 9: lấy ra số nhỏ nhất trong list: _list= [11, 2, 23, 45, 6, 9]
#Cơ bản
_list8 = [11, 2, 23, 45, 6, 9]
min1 = _list8[0]
for i8 in range(0, len(_list8)):
    if(_list8[i8] <= min1):
        min1 = _list8[i8]
print(min1)
#Nâng cao
print(min(_list8))

#Bài 10: copy một list cho trước thành một list mới.
#Cơ bản
_list9 = [11, 2, 23, 45, 6, 9] 
_list9_new = _list9.copy()
#Nâng cao
_list9_new2 = _list9
print(_list9_new)
print(_list9_new2)

#Bài 11: Nhập vào từ bàn phím số n và list cho trước, tìm các từ có độ dài lớn hơn n từ list đó.
n = int(input("Nhập số lượng phần tử: "))
list11 = []
for i11 in range(0, n):
    list11.append(input(f"Nhập phần tử {i11}: "))
list11_len = [len(ii11) for ii11 in list11]
print(max(list11_len))













