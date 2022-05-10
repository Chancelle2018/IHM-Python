# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 12:24:32 2021

@author: chane
"""


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1140, 713)
        MainWindow.setStyleSheet("background-color: rgb(199, 226, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.c = QtWidgets.QLineEdit(self.centralwidget)
        self.c.setGeometry(QtCore.QRect(300, 380, 113, 20))
        self.c.setStyleSheet("font: 75 12pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.c.setText("")
        self.c.setObjectName("c")
        self.a = QtWidgets.QLineEdit(self.centralwidget)
        self.a.setGeometry(QtCore.QRect(50, 380, 113, 20))
        self.a.setStyleSheet("font: 75 12pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.a.setObjectName("a")
        self.label_optimum = QtWidgets.QLabel(self.centralwidget)
        self.label_optimum.setGeometry(QtCore.QRect(170, 60, 731, 71))
        self.label_optimum.setStyleSheet("color: rgb(18, 12, 107);\n"
"font: 40pt \"Segoe Print\";\n"
"")
        self.label_optimum.setObjectName("label_optimum")
        self.pushButton_afficher = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_afficher.setGeometry(QtCore.QRect(10, 540, 171, 31))
        self.pushButton_afficher.setStyleSheet("\n"
"border-top-color: rgb(255, 255, 255);\n"
"border-bottom-color: rgb(255, 255, 255);\n"
"color: rgb(18, 12, 107);\n"
"font: 20pt \"Segoe Print\";")
        self.pushButton_afficher.setObjectName("pushButton_afficher")
        self.comboBox_methode = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_methode.setGeometry(QtCore.QRect(930, 260, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.comboBox_methode.setFont(font)
        self.comboBox_methode.setStyleSheet("font: 75 12pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.comboBox_methode.setObjectName("comboBox_methode")
        self.comboBox_methode.addItem("")
        self.comboBox_methode.addItem("")
        self.comboBox_methode.addItem("")
        self.comboBox_methode.addItem("")
        self.b = QtWidgets.QLineEdit(self.centralwidget)
        self.b.setGeometry(QtCore.QRect(180, 380, 113, 20))
        self.b.setStyleSheet("font: 75 12pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.b.setObjectName("b")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(200, 510, 471, 151))
        self.textEdit.setStyleSheet("font: 75 12pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 340, 791, 71))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.e = QtWidgets.QLineEdit(self.centralwidget)
        self.e.setGeometry(QtCore.QRect(550, 380, 113, 20))
        self.e.setStyleSheet("font: 75 12pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.e.setText("")
        self.e.setObjectName("e")
        self.f = QtWidgets.QLineEdit(self.centralwidget)
        self.f.setGeometry(QtCore.QRect(680, 380, 113, 20))
        self.f.setStyleSheet("font: 75 12pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.f.setText("")
        self.f.setObjectName("f")
        self.label_fo = QtWidgets.QLabel(self.centralwidget)
        self.label_fo.setGeometry(QtCore.QRect(20, 250, 361, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_fo.setFont(font)
        self.label_fo.setStyleSheet("color: rgb(18, 12, 107);\n"
"font: 20pt \"Segoe Print\";")
        self.label_fo.setObjectName("label_fo")
        self.x0 = QtWidgets.QLineEdit(self.centralwidget)
        self.x0.setGeometry(QtCore.QRect(870, 340, 113, 22))
        self.x0.setObjectName("x0")
        self.label_xo = QtWidgets.QLabel(self.centralwidget)
        self.label_xo.setGeometry(QtCore.QRect(840, 340, 31, 20))
        self.label_xo.setStyleSheet("font: 75 10pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label_xo.setObjectName("label_xo")
        self.epsilon = QtWidgets.QLineEdit(self.centralwidget)
        self.epsilon.setGeometry(QtCore.QRect(870, 390, 113, 22))
        self.epsilon.setObjectName("epsilon")
        self.label_epsilon = QtWidgets.QLabel(self.centralwidget)
        self.label_epsilon.setGeometry(QtCore.QRect(810, 390, 81, 20))
        self.label_epsilon.setStyleSheet("font: 75 10pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label_epsilon.setObjectName("label_epsilon")
        self.pas = QtWidgets.QLineEdit(self.centralwidget)
        self.pas.setGeometry(QtCore.QRect(1020, 390, 113, 22))
        self.pas.setObjectName("pas")
        self.label_pas = QtWidgets.QLabel(self.centralwidget)
        self.label_pas.setGeometry(QtCore.QRect(990, 390, 41, 16))
        self.label_pas.setStyleSheet("font: 75 10pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label_pas.setObjectName("label_pas")
        self.d = QtWidgets.QLineEdit(self.centralwidget)
        self.d.setGeometry(QtCore.QRect(430, 380, 113, 20))
        self.d.setStyleSheet("font: 75 12pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.d.setText("")
        self.d.setObjectName("d")
        self.x1_2 = QtWidgets.QLabel(self.centralwidget)
        self.x1_2.setGeometry(QtCore.QRect(1000, 340, 81, 20))
        self.x1_2.setStyleSheet("font: 75 10pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.x1_2.setObjectName("x1_2")
        self.x1 = QtWidgets.QLineEdit(self.centralwidget)
        self.x1.setGeometry(QtCore.QRect(1020, 340, 113, 22))
        self.x1.setObjectName("x1")
        self.tableWidget.raise_()
        self.c.raise_()
        self.a.raise_()
        self.label_optimum.raise_()
        self.pushButton_afficher.raise_()
        self.comboBox_methode.raise_()
        self.b.raise_()
        self.textEdit.raise_()
        self.e.raise_()
        self.f.raise_()
        self.label_fo.raise_()
        self.x0.raise_()
        self.label_xo.raise_()
        self.epsilon.raise_()
        self.label_epsilon.raise_()
        self.pas.raise_()
        self.label_pas.raise_()
        self.d.raise_()
        self.x1_2.raise_()
        self.x1.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1140, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "config ip"))
        self.label_optimum.setText(_translate("MainWindow", "Méthode non linéaire"))
        self.pushButton_afficher.setText(_translate("MainWindow", "Résultat"))
        self.comboBox_methode.setItemText(0, _translate("MainWindow", "Newton-Raphson"))
        self.comboBox_methode.setItemText(1, _translate("MainWindow", "Bissection"))
        self.comboBox_methode.setItemText(2, _translate("MainWindow", "Pas fixe"))
        self.comboBox_methode.setItemText(3, _translate("MainWindow", "Pas accéléré"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "f(x)"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "x^5"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "x^4"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "x^3"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "x^2"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "x"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "c"))
        self.label_fo.setText(_translate("MainWindow", "Fonction objective"))
        self.label_xo.setText(_translate("MainWindow", "x0"))
        self.label_epsilon.setText(_translate("MainWindow", "Epsilon"))
        self.label_pas.setText(_translate("MainWindow", "Pas"))
        self.x1_2.setText(_translate("MainWindow", "x1"))


        self.pushButton_afficher.clicked.connect(self.resultat)
    def resultat(self):
            if self.comboBox_methode.currentIndex()==0:
                self.textEdit.clear()


        
                eps= float(self.epsilon.text())
                xi= int(self.x0.text())
        
        
                def deriv1(x,a,b,c,d,e): 
                    return 5*a*(x**4) + 4*b*(x**3)+ 3*c*(x**2)+ 2*d*x + e
                def deriv2(x,a,b,c,d):
                    return 20*a*(x**3) + 12*b*(x**2)+ 6*c*x+ 2*d
      
        
                while True:
                        xf=xi-deriv1(xi,int(self.a.text()),int(self.b.text()),int(self.c.text()),int(self.d.text()),int(self.e.text()))/deriv2(xi, int(self.a.text()),int(self.b.text()),int(self.c.text()),int(self.d.text()))
                        if abs(deriv1(xf,int(self.a.text()),int(self.b.text()),int(self.c.text()),int(self.d.text()),int(self.e.text()))) <= eps:
                            break
                        xi=xf
        
                print (xf)
                self.textEdit.setText("Point optimum pour la fonction: " +str(xf))
            elif self.comboBox_methode.currentIndex()==1:
                a=float(self.a.text())
                b=float(self.b.text())
                c=float(self.c.text())
                d=float(self.d.text())
                e=float(self.e.text())
                f=float(self.f.text())
                epsilon=float(self.epsilon.text())
                x0=float(self.x0.text())
                x1=float(self.x1.text())

            def fct(x):
                return a*(x**5)+b*(x**4)+c*(x**3)+d*(x**2)+e*x+f
            
            def biss(a,b,epsilon,optimum):
                x0=(a+b)/2
                x1=(a+x0)/2
                x2=(x0+b)/2
                f0 = fct(x0)
                f1 = fct(x1)
                f2 = fct(x2)
                if optimum == 'mini':
                    if f2>f0 and f0>f1:
                        b=x0
                    elif f2<f0 and f0<f1:
                        a=x0
                    elif f1>f0 and f2>f0:
                        a=x1
                        b=x2
                elif optimum == 'maxi':
                    if f2>f0 and f0>f1:
                        a=x0
                    elif f2<f0 and f0<f1:
                        b=x0
                    elif f1>f0 and f2>f0:
                        if f1==max(f1,f2):
                            b=x1
                        else:
                            a=x2
                return(a,b)
            
            def b(a,b,optimum,epsilon):
                while (b-a)>epsilon:
                    (a,b)=biss(a,b,epsilon,optimum)
                print("a={0},b={1},x={2}".format(a,b,(a+b)/2))
            
                return (a+b)/2
            xf=b(x0,x1,'mini',epsilon)
            self.textEdit.setText("Point optimum pour la fonction: " +str(xf))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

