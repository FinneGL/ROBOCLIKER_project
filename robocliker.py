import sys
from PyQt6.QtCore import QSize, Qt, QRect, QPropertyAnimation, QSequentialAnimationGroup
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import *

class Roboclickergame(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Roboclickergame")
        self.load_pixmap()
        self.main_layout = QVBoxLayout()
        self.upgrade_layout = QHBoxLayout()

        button = QLabel()
        button.setAlignment(
            Qt.AlignmentFlag.AlignHCenter |
            Qt.AlignmentFlag.AlignVCenter
        )
        sprite_rect = QRect(0, 0, 48, 46 )
        self.sprite_pixmap = self.atlas_main.copy(sprite_rect)
        button.setPixmap(self.sprite_pixmap)

        self.main_layout.addWidget(button)
         
        widget = QWidget()
        widget.setLayout(self.main_layout)
        self.setCentralWidget(widget)

    def load_pixmap(self):
        self.atlas_main = QPixmap("Sprites/Clicker1.png")

        if self.atlas_main.isNull():
            print("Picture is not defined")
        
        self.atlas_upgrade = QPixmap("Sprites/Clicker1.png")

        if self.atlas_upgrade.isNull():
            print("Picture is not defined")

    def init_updgrate_layout(self):
        ...
        
    def became_button(self):
       ...
    
app = QApplication(sys.argv)

window = Roboclickergame()
window.show()

app.exec()