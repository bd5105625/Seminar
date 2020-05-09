import sys
from PyQt5 import QtCore, QtGui, Qt
# from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QVBoxLayout, QLabel, QPushButton, QListWidgetItem, \
    QHBoxLayout , QMainWindow, QLineEdit, QTableView, QFileDialog, QMessageBox
from PyQt5.QtCore import *
import pandas as pd
# from PyQt5.QtWidgets import QWidgets

class CustomQWidget(QWidget):
    def __init__(self , parent=None):
        super(CustomQWidget, self).__init__(parent)

    def setlist(self, num , orgfile , labelfile):
        index = QLabel()
        index.setText(str(num+1))
        index.setFixedSize(20,20)
        pic = QLabel()
        pic.setPixmap(QtGui.QPixmap(orgfile).scaled(150,150))  #control pixmap size by using scaled
        pic.setFixedSize(150,150)
        labelpic = QLabel()
        labelpic.setPixmap(QtGui.QPixmap(labelfile).scaled(150,150))
        labelpic.setFixedSize(150,150)
        filename = QLabel()
        filename.setText(orgfile.split('/')[-1])
        filename.setFixedSize(200,100)
        filename.setAlignment(QtCore.Qt.AlignCenter)
        layout = QHBoxLayout()
        layout.addWidget(index)
        layout.addWidget(pic)
        layout.addWidget(labelpic)
        layout.addWidget(filename)
        self.setLayout(layout)

class TabelView(QtCore.QAbstractTableModel):
    def __init__(self,data):
        super(TabelView, self).__init__()
        self._data = data
        self.list = []
    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]
    def rowCount(self, index):
        if type(self._data) == type(self.list):
            return len(self._data)
        return self._data.shape[0]
    def columnCount(self, index):
        # if len(self._data) != 0:
        if type(self._data) == type(self.list):
            return len(self._data[0])
        return self._data.shape[1]
    def inputdata(self,data):
        self._data = data

class ResultPage:
    def __init__(self, *args,**kwargs):
        self.newbutton()
    def newbutton(self):
        self.backtomenu = QPushButton()
        self.backtomenu.close()
    def setpage(self , filelist):
        self.window = QWidget()
        self.FirstLayout = QHBoxLayout(self.window)
        
        leftlayout = QVBoxLayout()
        self.name = QLabel(self)
        self.name.setFixedSize(200,100)
        self.name.setFont(QtGui.QFont("Times" , 14 , QtGui.QFont.Black))
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setStyleSheet("border-radius: 25px;border: 1px solid black;")
        leftlayout.addWidget(self.name)

        list = QListWidget()
        # filepath = "test.jpg"
        for i in range(0 , len(filelist)):
            print("time:", i)
            filepath = filelist[i]
            item = QListWidgetItem(list)
            item_widget = CustomQWidget()
            item_widget.setlist(i,filepath , filepath)
            item.setSizeHint(item_widget.sizeHint())
            list.addItem(item)
            list.setItemWidget(item, item_widget)
            # list.setFixedHeight(400)
        leftlayout.addWidget(list)

        rightlayout = QVBoxLayout()
        lb1 = QLabel()
        lb1.setFixedSize(200,100)
        rightlayout.addWidget(lb1)
        self.score = QLabel("80%")
        self.score.setFixedSize(200,100)
        self.score.setFont(QtGui.QFont("Times" , 32 , QtGui.QFont.Bold))
        self.score.setAlignment(QtCore.Qt.AlignCenter)
        # self.score.setStyleSheet("border-radius: 25px;border: 1px solid black;")
        rightlayout.addWidget(self.score)
        self.backtomenu.setFixedSize(200,100)
        self.backtomenu.setText("Back to Menu")
        self.backtomenu.setFont(QtGui.QFont("Times" , 16))
        self.backtomenu.setStyleSheet("background: transparent;")
        rightlayout.addWidget(self.backtomenu)
        lb2 = QLabel()
        lb2.setFixedSize(200,100)
        rightlayout.addWidget(lb2)

        self.FirstLayout.addLayout(leftlayout)
        self.FirstLayout.addLayout(rightlayout)
        # self.FirstLayout.setLab

    def initrtable(self,data):
        for i in range(0,len(data)):
            data[i].append("%")
        # data = pd.DataFrame(
        #     data,
        #     columns = ['Image Name' , 'Score']
        # )
        self.resulttable = QTableView(self)
        self.model = TabelView(data)
        self.resulttable.setModel(self.model)
        self.resulttable.resize(700,600)
        self.resulttable.move(100,100)
        # header = self.resulttable.horizontalHeader()
        # header.setStretchLastSection(True)
class UploadPage():
    # data = [[4],[1],[3],[3],[4]]
    def __init__(self, *args,**kwargs):
        # super(TabelView,self).__init__(self, *args,**kwargs)
        self.temp = []
        self.patient = QLineEdit(self)
        self.label1 = QLabel(self)
        self.label2 = QLabel(self)
        self.label3 = QLabel(self)
        # self.label2 = QLabel(self)
        self.date = QLineEdit(self)
        self.patient.setFont(QtGui.QFont("Times" , 16)),self.date.setFont(QtGui.QFont("Times" , 16))
        self.label1.setText("已上傳：0"),self.label2.setText("Patient No."),self.label3.setText("Date")
        self.label1.setFont(QtGui.QFont("Times" , 16))
        self.label2.setFont(QtGui.QFont("Times" , 10))
        self.label3.setFont(QtGui.QFont("Times" , 10))
        self.label1.setStyleSheet("border-radius: 25px;border: 1px solid black;")
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label3.setAlignment(QtCore.Qt.AlignCenter)
        # self.label2.setText("Patient 1")
        # self.label3.setText("2020/5/3")
        self.label1.resize(200,100),self.label2.resize(100,30),self.label3.resize(100,30)
        self.patient.resize(200,100),self.date.resize(200,100)
        self.label1.move(900,50),self.label2.move(950,170),self.label3.move(950,320)
        self.patient.move(900,200),self.date.move(900,350)
        self.label1.close(),self.label2.close(),self.label3.close(),self.patient.close(),self.date.close()
        self.result = QPushButton(self)
        self.choose = QPushButton(self)
        self.result.setStyleSheet("border-radius: 25px;border: 1px solid black;")
        self.choose.setStyleSheet("border-radius: 25px;border: 1px solid black;")
        self.result.setFont(QtGui.QFont("Times" , 16)),self.choose.setFont(QtGui.QFont("Times" , 16))
        self.result.setText("Result"),self.choose.setText("Upload")
        self.result.resize(200,100),self.choose.resize(200,100)
        self.result.move(900,650),self.choose.move(900,500)
        self.result.close(),self.choose.close()
    def showpageupload(self):
        self.label1.show(),self.label2.show(),self.label3.show()
        self.patient.show(),self.date.show(),self.result.show(),self.choose.show()
        self.inittable()
        self.table.show()
        self.patient.setText(""),self.date.setText("")
    def closepageupload(self):
        self.label1.close(),self.label2.close(),self.label3.close(),self.patient.close(),self.date.close(),self.result.close(),self.choose.close(),self.table.close()
    def openFileNamesDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.files, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)
        print(self.files)
        if self.files:
            for item in self.files:
                self.temp.append([]),self.temp[len(self.temp)-1].append(item.split('/')[-1])
        # print("temp" , len(self.temp))
        if len(self.temp) != 0:
            self.model = TabelView(self.temp)
            self.table.setModel(self.model)
        self.label1.setText("已上傳:" + str(len(self.temp)))
    def inittable(self):
        data = [
            ['']
        ]
        self.table = QTableView(self)
        self.model = TabelView(data)
        self.table.setModel(self.model)
        self.table.resize(600,600)
        self.table.move(100,100)
        header = self.table.horizontalHeader()
        header.setStretchLastSection(True)
class SecondPage:
    def __init__(self, *args, **kwargs):
        self.upload = QPushButton(self)
        self.developer = QPushButton(self)
        self.upload.setText("Upload")
        self.developer.setText("Developer")
        self.upload.setStyleSheet("background: transparent;"),self.developer.setStyleSheet("background: transparent;")
        self.upload.setFont(QtGui.QFont("Times" , 16)),self.developer.setFont(QtGui.QFont("Times" , 16))
        self.upload.resize(200,100),self.developer.resize(200,100)
        self.upload.move(500,250),self.developer.move(500,450)
        self.upload.close(),self.developer.close()
    def showpage2(self):
        self.upload.show(),self.developer.show()
    def closepage2(self):
        self.upload.close(),self.developer.close()

class FirstWindow(QMainWindow,SecondPage,UploadPage,ResultPage):
    def __init__(self, *args, **kwargs):
        super(FirstWindow, self).__init__(*args , **kwargs)
        super(SecondPage,self).__init__(*args , **kwargs)
        super(UploadPage,self).__init__(*args , **kwargs)
        super(ResultPage,self).__init__(*args, **kwargs)
        self.setWindowTitle("Window Title")
        self.setGeometry(800,800,1200,800)
        self.initbutton()
        self.clickbutton()
    def initbutton(self):
        self.icon = QLabel(self)
        self.icon.setFont(QtGui.QFont("Times" , 18 , QtGui.QFont.Bold))
        self.icon.setStyleSheet("border-radius: 25px;border: 2px solid black;")
        self.icon.setAlignment(QtCore.Qt.AlignCenter)
        self.startbutton = QPushButton(self)
        self.startbutton.setFont(QtGui.QFont("Times" , 18))
        self.startbutton.setStyleSheet("background: transparent;")
        self.icon.setText("ILD DIAGNOSIS"),self.startbutton.setText("Enter")
        self.icon.resize(300,150),self.startbutton.resize(200,100)
        self.icon.move(450,250),self.startbutton.move(500 , 400)
        self.icon.show(),self.startbutton.show()
    def clickbutton(self):
        self.startbutton.clicked.connect(self.clickstart)
        self.upload.clicked.connect(self.clickupload)
        self.result.clicked.connect(self.clickresult)
        self.choose.clicked.connect(self.clickchoose)
        self.backtomenu.clicked.connect(self.clickbacktomenu)
    def clickstart(self):
        self.icon.close(),self.startbutton.close()
        super(FirstWindow,self).showpage2()
        # super(SecondPage,self).showpage2()
    def clickupload(self):
        super(FirstWindow,self).closepage2()
        super(FirstWindow,self).showpageupload()
    def clickresult(self):
        if len(self.temp) == 0:
            QMessageBox.about(self,'Warning', u"Please upload picture!")
            print(self.patient.text() , self.date.text())
        elif self.patient.text() == "" or self.date.text() == "":
            QMessageBox.about(self,'Warning', u"Please enter patient name and date")
        else:
            super(FirstWindow,self).closepageupload()
            # super(FirstWindow,self).showresultpage(self.temp)
            super(FirstWindow,self).setpage(self.files)
            self.setCentralWidget(self.window)
            self.name.setText(self.patient.text())
    def clickchoose(self):
        super(FirstWindow,self).openFileNamesDialog()
    def clickbacktomenu(self):
        # super(FirstWindow,self).closeresultpage()
        super(FirstWindow,self).showpage2()
        super(FirstWindow,self).newbutton()
        self.backtomenu.clicked.connect(self.clickbacktomenu)
        self.temp = []
        self.window.setParent(None) #close result page's layout

if __name__ == '__main__':
    print('__name__' , __name__)
    app = QApplication(sys.argv)
    window = FirstWindow()
    window.show()
    app.exec_()
