import smtplib
from email.mime.text import MIMEText
import datetime

def send_email(sender_email, sender_password, recipient_email, subject, body_html):
    try:
        # Tạo nội dung email với HTML
        msg = MIMEText(body_html, "html")
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = recipient_email

        # Kết nối và gửi email
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())

        print("Email đã được gửi thành công!")
    except Exception as e:
        print(f"Không thể gửi email. Lỗi: {e}")

# Nội dung HTML
body_html = """
<html>
    <body>
        <h2 style="color: #2E86C1;">Xin chào!</h2>
        <p style="font-size: 16px;">Đây là email gửi từ Python.</p>
        <p style="color: #555;">Chúc bạn một ngày tốt lành!</p>
        <hr>
        <footer style="font-size: 12px; color: #999;">Email tự động, vui lòng không trả lời.</footer>
    </body>
</html>
"""

#kiểm tra thời gian xử lý
start = datetime.datetime.now()
# Gửi email
send_email(
    sender_email="kariatnguyen+spam@gmail.com",         # Thay bằng email của bạn
    sender_password="vdfo ilek uknu dhuy",             # Thay bằng mật khẩu hoặc mật khẩu ứng dụng
    recipient_email="20214044@eaut.edu.vn",  # Email người nhận
    subject="Email HTML đẹp hơn",
    body_html=body_html
)
end = datetime.datetime.now()
print("Thời gian xử lý:", end - start)