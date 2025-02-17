
import Module.Mauchu as mc

strA = input("Nhập chuỗi: ")
print(f"{mc.GREEN}Viết ngược lại: {mc.RESET}", end="")
for i in range(1, len(strA)+1):
    print(strA[-i], end="")

print()
key = input(f"{mc.GREEN}Từ cần tìm: {mc.RESET}")
print("Kí tự '"+ key +"' được lặp" ,strA.count(key))

print("Tổng ",len(strA)," kí trị có trong chuỗi")

print("Câu đã được định dạng:", strA.title()+".")


print("Viết hoa:", strA.title())

a = ""
for j in range(len(strA)):
    if strA[j] != " ":
        a += strA[j]
    elif j > 0 and strA[j-1] != " ":
        a += " " 
print("Định dạng chuẩn:",a.title())

dem = 0
for k in range(0,len(strA)-1) :
    if strA[k] != " " and strA[k+1] == " ":
        dem += 1
print("Có", dem, "từ trong chuỗi")

# In biến đầu và kết thúc
for k1 in range(0, len(strA)):
    if strA[k1] != " ":
        print("Biến đầu là: ", strA[k1])
        break

for k12 in range(0, -len(strA),-1):
    if strA[k12] != " ":
        print("Biến kết thúc là: ", strA[k12])
        break