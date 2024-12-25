import requests
import sys
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QWidget
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class Login_window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login page')
        self.setGeometry(300, 300, 650, 650)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)

        #login_title
        self.title_label = QLabel('login to your account')
        self.title_label.setFont(QFont('Arial', 16))
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #add_widgets_to_layout
        layout.addWidget(self.title_label)

        self.setLayout(layout)


def receive_data():
    pass

def send_data():
    pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Login_window()
    window.show()
    sys.exit(app.exec())
