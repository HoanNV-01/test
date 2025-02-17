from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
import os
import datetime
import smtplib
from email.mime.text import MIMEText


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(633, 397)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txt_content = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.txt_content.setGeometry(QtCore.QRect(10, 110, 341, 191))
        self.txt_content.setObjectName("txt_content") # Phần này chính là nội dung email
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 80, 341, 31))
        self.label.setObjectName("label")
        self.txt_email = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.txt_email.setGeometry(QtCore.QRect(360, 80, 261, 151))
        self.txt_email.setObjectName("txt_email") # Phần này chính là email người nhận
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(370, 50, 241, 21))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(490, 270, 121, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 240, 121, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(370, 240, 121, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(370, 270, 121, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.txt_Note = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.txt_Note.setGeometry(QtCore.QRect(10, 310, 611, 81))
        self.txt_Note.setObjectName("txt_Note") # Phần này chính là thông báo
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 61, 21))
        self.label_3.setObjectName("label_3")
        self.txt_title = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.txt_title.setGeometry(QtCore.QRect(70, 50, 281, 31))
        self.txt_title.setObjectName("txt_title") # Phần này chính là tiêu đề email
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 611, 41))
        self.label_4.setObjectName("label_4")
        self.label_3.raise_()
        self.txt_content.raise_()
        self.label.raise_()
        self.txt_email.raise_()
        self.label_2.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.txt_Note.raise_()
        self.txt_title.raise_()
        self.label_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.txt_Note.setPlainText('')
        # Xử lý sự kiện
        self.pushButton.clicked.connect(self.send_email)
        self.pushButton_2.clicked.connect(self.refresh_all)
        self.pushButton_3.clicked.connect(self.refresh_content)
        self.pushButton_4.clicked.connect(self.refresh_email)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tool Send Mail"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Enter email content</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Email</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Send"))
        self.pushButton_2.setText(_translate("MainWindow", "Refresh All"))
        self.pushButton_3.setText(_translate("MainWindow", "Refresh Content"))
        self.pushButton_4.setText(_translate("MainWindow", "Refresh Email"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Title:</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Tool Send Mail</span></p></body></html>"))
    
    def send_email(self):
        # Lấy thông tin từ giao diện
        email = self.txt_email.toPlainText()
        title = self.txt_title.toPlainText()
        content = self.txt_content.toPlainText()
        # Tách các email bằng dấu phẩy
        email_list = [email.strip() for email in email.split(",") if email.strip()]
        print(email_list)
        
        # Kiểm tra email và nội dung
        if not email or not title or not content:
            QMessageBox.warning(None, "Thiếu thông tin", "Vui lòng nhập đầy đủ nội dung và email!")
        else:
            send_success, send_failed = 0, 0
            for email in email_list:
                # Gửi email
                send = call_send_email( sender_email="kariatnguyen+spam@gmail.com", sender_password="vdfo ilek uknu dhuy", recipient_email=email, subject=title, body_html=content)
                if send == True:
                    self.txt_Note.insertPlainText(f"Email sent successfully to {email} at {str(datetime.datetime.now())} \n")
                    send_success += 1
                else:
                    self.txt_Note.insertPlainText(f"Email sent failed to {email} at {str(datetime.datetime.now())} \n Error: {send} \n")
                    send_failed += 1
            # Hiển thị hộp cảnh báo
            if len(email_list) > 1: QMessageBox.warning(None, 'Email sending status', f'Sent: {send_success}, Sent failed: {send_failed}')
            return
    
    def refresh_all(self):
        self.txt_email.setPlainText("")
        self.txt_title.setPlainText("")
        self.txt_content.setPlainText("")
        
    def refresh_content(self):
        self.txt_content.setPlainText("")
        
    def refresh_email(self):
        self.txt_email.setPlainText("")
    
def call_send_email(sender_email, sender_password, recipient_email, subject, body_html):
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
        return True
    except Exception as e:
        return e   

if __name__ == "__main__":
    import sys
    global Note
    Note = ""
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
