from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(975, 584)


        self.image_capture = QtWidgets.QPushButton(Dialog)
        self.image_capture.setGeometry(QtCore.QRect(860, 10, 80, 71))
        self.image_capture.setObjectName("image_capture")

        self.filename = QtWidgets.QTextEdit(Dialog)
        self.filename.setGeometry(QtCore.QRect(620, 10, 221, 70))
        self.filename.setObjectName("filename")

        self.quit = QtWidgets.QPushButton(Dialog)
        self.quit.setGeometry(QtCore.QRect(860, 490, 80, 71))
        self.quit.setObjectName("quit")

        self.loading_status = QtWidgets.QLabel(Dialog)
        self.loading_status.setGeometry(QtCore.QRect(840, 110, 131, 51))
        self.loading_status.setObjectName("loading_status")

        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(20, 100, 561, 451))
        self.graphicsView.setObjectName("graphicsView")
        
        ##
        # change_folder_action.triggered.connect(self.change_folder)

        self.image_capture.clicked.connect(self.pressed)
        self.quit.clicked.connect(self.closeEvent)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.image_capture.setText(_translate("Dialog", "Capture"))
        self.quit.setText(_translate("Dialog", "Quit"))
        self.loading_status.setText(_translate("Dialog", "TextLabel"))

    def pressed(self):
        textboxval = self.filename.toPlainText()
        # print(type(textboxval))


    def closeEvent(self):
        # self.camera.exit()
        sys.exit(app.exec_())
        # return Ui_Dialog.closeEvent()

    def change_folder(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(self,"Picture Location", "")
        if path:
            self.save_path = path
            self.save_seq = 0
            #add obj later


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
