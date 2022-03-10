from PyQt5 import QtWidgets

def pop_up(title, text):
    msg = QtWidgets.QMessageBox()
    msg.setWindowTitle(title)
    msg.setText(text)
    msg.exec()
