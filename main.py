from PyQt5.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout, QWidget, QLabel, QListWidget, QPushButton, QFileDialog, QMessageBox
import os
from PIL import Image, ImageOps, ImageFilter
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
class ImageProcessor():
    def __init__(self):
        self.filename = None
        self.Image = None
        self.dir = None
        self.save_dir = 'Modified/'
    def loadImage(self, filename):
        self.filename = filename
        self.dir = workdir
        image_path = os.path.join(self.dir, self.filename)
        self.Image = Image.open(image_path)
    def showImage(self, path):
        pixmapimage = QPixmap(path)
        label_width = pic.width()
        label_height = pic.height()
        scaled_pixmap = pixmapimage.scaled(label_width, label_height, Qt.KeepAspectRatio)
        pic.setPixmap(scaled_pixmap)
        pic.setVisible(True)
    def saveImage(self):
        path = os.path.join(self.dir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.Image.save(image_path)
    def do_bw(self):
        if pic_list.selectedItems():
            self.Image = ImageOps.grayscale(self.Image)
            self.saveImage()
            Image_path = os.path.join(self.dir, self.save_dir, self.filename)
            self.showImage(Image_path)
        else:
            error_win = QMessageBox()
            error_win.setText('нажмите "Папка" и выберите картинку')
            error_win.exec()
    def do_left(self):
        if pic_list.selectedItems():
            self.Image = self.Image.rotate(90)
            self.saveImage()
            Image_path = os.path.join(self.dir, self.save_dir, self.filename)
            self.showImage(Image_path)
        else:
            error_win = QMessageBox()
            error_win.setText('нажмите "Папка" и выберите картинку')
            error_win.exec()
    def do_right(self):
        if pic_list.selectedItems():
            self.Image = self.Image.rotate(-90)
            self.saveImage()
            Image_path = os.path.join(self.dir, self.save_dir, self.filename)
            self.showImage(Image_path)
        else:
            error_win = QMessageBox()
            error_win.setText('нажмите "Папка" и выберите картинку')
            error_win.exec()
    def do_mirror(self):
        if pic_list.selectedItems():
            self.Image = ImageOps.mirror(self.Image)
            self.saveImage()
            Image_path = os.path.join(self.dir, self.save_dir, self.filename)
            self.showImage(Image_path)
        else:
            error_win = QMessageBox()
            error_win.setText('нажмите "Папка" и выберите картинку')
            error_win.exec()
    def do_sharpen(self):
        if pic_list.selectedItems():
            try:
                self.Image = self.Image.filter(ImageFilter.SHARPEN)
            except:
                error_win = QMessageBox()
                error_win.setText('не могу ):')
            self.saveImage()
            Image_path = os.path.join(self.dir, self.save_dir, self.filename)
            self.showImage(Image_path)
        else:
            error_win = QMessageBox()
            error_win.setText('нажмите "Папка" и выберите картинку')
            error_win.exec()
workimage = ImageProcessor()
def showChosenImage():
    if pic_list.currentRow() >= 0:
        filename = pic_list.currentItem().text()
        workimage.loadImage(filename)
        Image_path = os.path.join(workimage.dir, filename)
        workimage.showImage(Image_path)

workdir = ""
def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
def filter(files, extensions):
    result = []
    for filename in files:
        for extension in extensions:
            if filename.endswith(extension):
                result.append(filename)
    return result
def showFilenamesList():
    chooseWorkdir()
    extensions = ['.jpg', '.jpeg', '.png', '.gif']
    files = os.listdir(workdir)
    files = filter(files, extensions)
    pic_list.clear()
    pic_list.addItems(files)
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Easy Editor')
main_win.resize(700, 500)
btn1 = QPushButton('Папка')
btn2 = QPushButton('Лево')
btn3 = QPushButton('Право')
btn4 = QPushButton('Зеркало')
btn5 = QPushButton('Резкость')
btn6 = QPushButton("Ч/Б")
pic = QLabel('Картинка')
pic_list = QListWidget()
h_line1 = QHBoxLayout()
h_line2 = QHBoxLayout()
v_line1 = QVBoxLayout()
v_line2 = QVBoxLayout()
main_win.setLayout(h_line1)
h_line1.addLayout(v_line1)
h_line1.addLayout(v_line2)
v_line1.addWidget(btn1)
v_line2.addWidget(pic)
v_line2.addLayout(h_line2)
v_line1.addWidget(pic_list)
h_line2.addWidget(btn2)
h_line2.addWidget(btn3)
h_line2.addWidget(btn4)
h_line2.addWidget(btn5)
h_line2.addWidget(btn6)
btn1.clicked.connect(showFilenamesList)
pic_list.currentRowChanged.connect(showChosenImage)
btn6.clicked.connect(workimage.do_bw)
btn2.clicked.connect(workimage.do_left)
btn3.clicked.connect(workimage.do_right)
btn4.clicked.connect(workimage.do_mirror)
btn5.clicked.connect(workimage.do_sharpen)
main_win.show()
app.exec()