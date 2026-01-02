from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class Greeting_Window(QMainWindow):

    def __init__(self):
        super(Greeting_Window, self).__init__()
        self.setGeometry(200, 200, 640, 480)
        self.setWindowTitle("Greeting")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText(
            "Welcome to Nexa Password Manager\n\n\n"
        "Securely store and access your passwords from anywhere.\n\n\n"
        "Secure • Convenient • Open Source"
        )
        self.label.move(50, 50)
        self.update()

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Continue")
        self.b1.move(50, 200)
        self.b1.clicked.connect(self.button_press)


    def button_press(self):
        self.label.setText("You pressed the button.")
        self.update()

    def update(self):
        self.label.adjustSize()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Greeting_Window()
    win.show()
    sys.exit(app.exec_())
