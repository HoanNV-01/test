import base64

# Dữ liệu cần mã hóa
original_data = "Đây là chuỗi cần mã hóa!"

# Chuyển chuỗi sang bytes (Base64 làm việc với bytes)
byte_data = original_data.encode('utf-8')

# Mã hóa Base64
encoded_data = base64.b64encode(byte_data)

# Kết quả là bytes, chuyển thành chuỗi để dễ đọc
encoded_string = encoded_data.decode('utf-8')

print(f"Dữ liệu gốc: {original_data}")
print(f"Dữ liệu mã hóa: {encoded_string}")
