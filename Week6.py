# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)

        self.horizontalSlider = QtWidgets.QSlider(Form)
        self.horizontalSlider.setGeometry(QtCore.QRect(100, 100, 261, 21))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setMinimum(8)
        self.horizontalSlider.setMaximum(40)
        self.horizontalSlider.setValue(12)
        self.horizontalSlider.setObjectName("horizontalSlider")

        self.horizontalSlider_2 = QtWidgets.QSlider(Form)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(100, 150, 261, 21))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setMinimum(0)
        self.horizontalSlider_2.setMaximum(255)
        self.horizontalSlider_2.setValue(255)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")

        self.horizontalSlider_3 = QtWidgets.QSlider(Form)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(100, 200, 261, 21))
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setMinimum(0)
        self.horizontalSlider_3.setMaximum(255)
        self.horizontalSlider_3.setValue(0)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")

        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(50, 20, 301, 61))
        self.textBrowser.setObjectName("textBrowser")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 100, 47, 13))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 150, 91, 21))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 200, 61, 16))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Set initial text
        self.textBrowser.setText("F1D022124")

        # Connect sliders
        self.horizontalSlider.valueChanged.connect(self.updateFontSize)
        self.horizontalSlider_2.valueChanged.connect(self.updateBackgroundColor)
        self.horizontalSlider_3.valueChanged.connect(self.updateFontColor)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Font and Color Adjuster - Ida Ayu Vinaya Anindya (F1D022124)"))
        self.label.setText(_translate("Form", "Font Size"))
        self.label_2.setText(_translate("Form", "Background Color"))
        self.label_3.setText(_translate("Form", "Font Color"))

    def updateFontSize(self):
        size = self.horizontalSlider.value()
        self.textBrowser.setStyleSheet(f"font-size: {size}px;")

    def updateBackgroundColor(self):
        value = self.horizontalSlider_2.value()
        color = f"rgb({value},{value},{value})"
        existing_style = self.textBrowser.styleSheet()
        self.textBrowser.setStyleSheet(existing_style + f" background-color: {color};")

    def updateFontColor(self):
        value = self.horizontalSlider_3.value()
        color = f"rgb({value},0,0)"
        existing_style = self.textBrowser.styleSheet()
        self.textBrowser.setStyleSheet(existing_style + f" color: {color};")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
