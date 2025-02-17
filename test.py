import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, body):
    try:
        # Thiết lập máy chủ SMTP (ở đây là Gmail)
        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        # Tạo email
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = recipient_email
        msg["Subject"] = subject

        # Nội dung email
        msg.attach(MIMEText(body, "plain"))

        # Kết nối đến máy chủ SMTP
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Bật mã hóa TLS
        server.login(sender_email, sender_password)

        # Gửi email
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()

        print("Email đã được gửi thành công!")

    except Exception as e:
        print(f"Không thể gửi email. Lỗi: {e}")

# Thông tin gửi email
sender_email = "kariatnguyen@gmail.com"  # Thay bằng email của bạn
sender_password = "vdfo ilek uknu dhuy"  # Thay bằng mật khẩu của bạn
recipient_email = "20214044@eaut.edu.vn"  # Email người nhận
subject = "Tiêu đề email"
body = "Nội dung email gửi từ Python."

# Gửi email
send_email(sender_email, sender_password, recipient_email, subject, body)
