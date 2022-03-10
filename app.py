from PyQt5 import QtWidgets, uic



# Initialize the application
app = QtWidgets.QApplication([])
window = uic.loadUi('gui/ui/main.ui')



# Show the application
window.show()
app.exec()
