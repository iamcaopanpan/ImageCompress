import sys
import os

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QLabel, QLineEdit, QHBoxLayout
from PyQt5.QtWidgets import QFileDialog, QSlider, QMessageBox
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt

import compress

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('图片压缩')
        self.setWindowIcon(QIcon('.././icon/Qt.png'))
        self.setFixedSize(500, 500)
        self.setStyleSheet('QLabel{Font-size:14pt; Font-Family: Microsoft YaHei UI}'
                           'QLineEdit{Font-size:14pt; Font-Family: Courier New; color: green}'
                           'QPushButton{Font-size:14pt; Font-Family: Microsoft YaHei UI}; Width:50px')

        self.initUi()
    def initUi(self):
        contain = QVBoxLayout()

        btn1 = QPushButton('打开一张图片')
        btn1.clicked.connect(self.btn1Clicked)

        h1 = QHBoxLayout()
        h2 = QHBoxLayout()
        h3 = QHBoxLayout()
        label1 = QLabel('图片路径：')
        label2 = QLabel('压缩前大小：')
        label3 = QLabel('压缩后大小：')
        self.line1 = QLineEdit()
        self.line2 = QLineEdit()
        self.label4 = QLabel()
        self.label4.setStyleSheet('Font-family: Courier New; Color: blue; Font-weight:bold')
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(100)
        self.slider.setMaximum(300)
        self.slider.setSingleStep(50)
        self.slider.setValue(150)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(50)
        self.slider.valueChanged.connect(self.sliderChanged)
        self.label_image = QLabel()          #显示图片
        self.label_image.resize(300, 300)
        h4 = QHBoxLayout()
        h4.addStretch()
        btn2 = QPushButton('压缩')
        btn2.clicked.connect(self.btn2Clicked)
        h4.addWidget(btn2)
        h4.addStretch()
        h1.addWidget(label1)
        h1.addWidget(self.line1)
        h2.addWidget(label2)
        h2.addWidget(self.line2)
        h3.addWidget(label3)
        self.label4.setText(str(self.slider.value()) + 'KB')
        h3.addWidget(self.label4)
        h3.addWidget(self.slider)

        contain.addWidget(btn1)
        contain.addLayout(h1)
        contain.addLayout(h2)
        contain.addLayout(h3)
        contain.addLayout(h4)
        contain.addWidget(self.label_image)

        self.setLayout(contain)
    def btn1Clicked(self):
        image1, _ = QFileDialog.getOpenFileName(self, '打开图片', 'D:/iamca/Pictures', '图片文件 (*.jpg *.png)')
        self.label_image.setPixmap(QPixmap(image1))
        self.label_image.setScaledContents(True)

        self.line1.setText(image1)
        self.line2.setText(str(os.path.getsize(image1)//1024)+' KB')
    def sliderChanged(self):
        self.label4.setText(str(self.slider.value()) + 'KB')
    def btn2Clicked(self):
        try:
            compress.compressImage(self.line1.text(), self.slider.value())

            QMessageBox.information(self, '成功', '已保存压缩后的图片', QMessageBox.Ok)
        except:pass




if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = Window()
    w.show()

    app.exec_()