import sys
from PyQt6.QtCore import QSize, Qt, QRect
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel

class Roboclickergame(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Roboclickergame")

        self.add_main_widget()

    def add_main_widget(self):
        widget = QLabel()

        self.atlas_pixmap = QPixmap("Sprites/Clicker1.png")

        if self.atlas_pixmap.isNull():
            print("Picture is not defined")

        widget.setPixmap(self.atlas_pixmap)

        widget.setAlignment(
            Qt.AlignmentFlag.AlignHCenter |
            Qt.AlignmentFlag.AlignVCenter
        )

        self.setCentralWidget(widget)

        sprite_rect = QRect(0, 0, 48, 46 )
        self.sprite_pixmap = self.atlas_pixmap.copy(sprite_rect)

    def find_one(self):
        ...


app = QApplication(sys.argv)

window = Roboclickergame()
window.show()

app.exec()