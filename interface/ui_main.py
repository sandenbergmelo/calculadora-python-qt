# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QActionGroup, QBrush, QColor,
    QConicalGradient, QCursor, QFont, QFontDatabase,
    QGradient, QIcon, QImage, QKeySequence,
    QLinearGradient, QPainter, QPalette, QPixmap,
    QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(336, 409)
        self.actionAutoCalc = QAction(MainWindow)
        self.actionAutoCalc.setObjectName(u"actionAutoCalc")
        self.actionAutoCalc.setCheckable(True)
        self.actionAutoCalc.setChecked(True)
        self.actionAutoCalc.setMenuRole(QAction.PreferencesRole)
        self.themesGroup = QActionGroup(MainWindow)
        self.themesGroup.setObjectName(u"themesGroup")
        self.actionThemeDefault = QAction(self.themesGroup)
        self.actionThemeDefault.setObjectName(u"actionThemeDefault")
        self.actionThemeDefault.setCheckable(True)
        self.actionThemeDefault.setMenuRole(QAction.PreferencesRole)
        self.actionThemeDracula = QAction(self.themesGroup)
        self.actionThemeDracula.setObjectName(u"actionThemeDracula")
        self.actionThemeDracula.setCheckable(True)
        icon = QIcon()
        iconThemeName = u"Theme"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.actionThemeDracula.setIcon(icon)
        self.actionThemeDracula.setMenuRole(QAction.PreferencesRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnC = QPushButton(self.centralwidget)
        self.btnC.setObjectName(u"btnC")
        self.btnC.setGeometry(QRect(40, 110, 51, 41))
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(18)
        font.setBold(True)
        self.btnC.setFont(font)
        self.btnCE = QPushButton(self.centralwidget)
        self.btnCE.setObjectName(u"btnCE")
        self.btnCE.setGeometry(QRect(100, 110, 51, 41))
        self.btnCE.setFont(font)
        self.btnDelete = QPushButton(self.centralwidget)
        self.btnDelete.setObjectName(u"btnDelete")
        self.btnDelete.setGeometry(QRect(160, 110, 51, 41))
        self.btnDelete.setFont(font)
        self.btnNumber1 = QPushButton(self.centralwidget)
        self.btnNumber1.setObjectName(u"btnNumber1")
        self.btnNumber1.setGeometry(QRect(40, 260, 51, 41))
        self.btnNumber1.setFont(font)
        self.btnNumber8 = QPushButton(self.centralwidget)
        self.btnNumber8.setObjectName(u"btnNumber8")
        self.btnNumber8.setGeometry(QRect(100, 160, 51, 41))
        self.btnNumber8.setFont(font)
        self.btnNumber9 = QPushButton(self.centralwidget)
        self.btnNumber9.setObjectName(u"btnNumber9")
        self.btnNumber9.setGeometry(QRect(160, 160, 51, 41))
        self.btnNumber9.setFont(font)
        self.btnNumber4 = QPushButton(self.centralwidget)
        self.btnNumber4.setObjectName(u"btnNumber4")
        self.btnNumber4.setGeometry(QRect(40, 210, 51, 41))
        self.btnNumber4.setFont(font)
        self.btnNumber5 = QPushButton(self.centralwidget)
        self.btnNumber5.setObjectName(u"btnNumber5")
        self.btnNumber5.setGeometry(QRect(100, 210, 51, 41))
        self.btnNumber5.setFont(font)
        self.btnNumber7 = QPushButton(self.centralwidget)
        self.btnNumber7.setObjectName(u"btnNumber7")
        self.btnNumber7.setGeometry(QRect(40, 160, 51, 41))
        self.btnNumber7.setFont(font)
        self.btnNumber6 = QPushButton(self.centralwidget)
        self.btnNumber6.setObjectName(u"btnNumber6")
        self.btnNumber6.setGeometry(QRect(160, 210, 51, 41))
        self.btnNumber6.setFont(font)
        self.btnNumber2 = QPushButton(self.centralwidget)
        self.btnNumber2.setObjectName(u"btnNumber2")
        self.btnNumber2.setGeometry(QRect(100, 260, 51, 41))
        self.btnNumber2.setFont(font)
        self.btnNumber3 = QPushButton(self.centralwidget)
        self.btnNumber3.setObjectName(u"btnNumber3")
        self.btnNumber3.setGeometry(QRect(160, 260, 51, 41))
        self.btnNumber3.setFont(font)
        self.btnNumber0 = QPushButton(self.centralwidget)
        self.btnNumber0.setObjectName(u"btnNumber0")
        self.btnNumber0.setGeometry(QRect(100, 310, 51, 41))
        self.btnNumber0.setFont(font)
        self.output = QLineEdit(self.centralwidget)
        self.output.setObjectName(u"output")
        self.output.setGeometry(QRect(40, 30, 251, 41))
        self.output.setFont(font)
        self.output.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.output.setReadOnly(True)
        self.btnComma = QPushButton(self.centralwidget)
        self.btnComma.setObjectName(u"btnComma")
        self.btnComma.setGeometry(QRect(160, 310, 51, 41))
        self.btnComma.setFont(font)
        self.btnPlus = QPushButton(self.centralwidget)
        self.btnPlus.setObjectName(u"btnPlus")
        self.btnPlus.setGeometry(QRect(240, 260, 51, 41))
        self.btnPlus.setFont(font)
        self.btnMinus = QPushButton(self.centralwidget)
        self.btnMinus.setObjectName(u"btnMinus")
        self.btnMinus.setGeometry(QRect(240, 210, 51, 41))
        self.btnMinus.setFont(font)
        self.btnMultiply = QPushButton(self.centralwidget)
        self.btnMultiply.setObjectName(u"btnMultiply")
        self.btnMultiply.setGeometry(QRect(240, 160, 51, 41))
        self.btnMultiply.setFont(font)
        self.btnDivide = QPushButton(self.centralwidget)
        self.btnDivide.setObjectName(u"btnDivide")
        self.btnDivide.setGeometry(QRect(240, 110, 51, 41))
        self.btnDivide.setFont(font)
        self.btnPower = QPushButton(self.centralwidget)
        self.btnPower.setObjectName(u"btnPower")
        self.btnPower.setGeometry(QRect(40, 310, 51, 41))
        self.btnPower.setFont(font)
        self.btnEqual = QPushButton(self.centralwidget)
        self.btnEqual.setObjectName(u"btnEqual")
        self.btnEqual.setGeometry(QRect(240, 310, 51, 41))
        self.btnEqual.setFont(font)
        self.btnEqual.setStyleSheet(u"")
        self.separator = QFrame(self.centralwidget)
        self.separator.setObjectName(u"separator")
        self.separator.setGeometry(QRect(220, 110, 16, 241))
        self.separator.setFrameShape(QFrame.VLine)
        self.separator.setFrameShadow(QFrame.Sunken)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 336, 21))
        self.menuConfig = QMenu(self.menubar)
        self.menuConfig.setObjectName(u"menuConfig")
        self.menuTema = QMenu(self.menuConfig)
        self.menuTema.setObjectName(u"menuTema")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuConfig.menuAction())
        self.menuConfig.addAction(self.actionAutoCalc)
        self.menuConfig.addSeparator()
        self.menuConfig.addAction(self.menuTema.menuAction())
        self.menuTema.addAction(self.actionThemeDefault)
        self.menuTema.addAction(self.actionThemeDracula)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculadora", None))
        self.actionAutoCalc.setText(QCoreApplication.translate("MainWindow", u"Calcular automaticamente", None))
        self.actionThemeDefault.setText(QCoreApplication.translate("MainWindow", u"Padr\u00e3o", None))
#if QT_CONFIG(tooltip)
        self.actionThemeDefault.setToolTip(QCoreApplication.translate("MainWindow", u"Theme", None))
#endif // QT_CONFIG(tooltip)
        self.actionThemeDracula.setText(QCoreApplication.translate("MainWindow", u"Dracula", None))
        self.btnC.setText(QCoreApplication.translate("MainWindow", u"C", None))
#if QT_CONFIG(shortcut)
        self.btnC.setShortcut(QCoreApplication.translate("MainWindow", u"Del", None))
#endif // QT_CONFIG(shortcut)
        self.btnCE.setText(QCoreApplication.translate("MainWindow", u"CE", None))
#if QT_CONFIG(shortcut)
        self.btnCE.setShortcut(QCoreApplication.translate("MainWindow", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.btnDelete.setText(QCoreApplication.translate("MainWindow", u"\u21d0", None))
#if QT_CONFIG(shortcut)
        self.btnDelete.setShortcut(QCoreApplication.translate("MainWindow", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.btnNumber1.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(shortcut)
        self.btnNumber1.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.btnNumber8.setText(QCoreApplication.translate("MainWindow", u"8", None))
#if QT_CONFIG(shortcut)
        self.btnNumber8.setShortcut(QCoreApplication.translate("MainWindow", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.btnNumber9.setText(QCoreApplication.translate("MainWindow", u"9", None))
#if QT_CONFIG(shortcut)
        self.btnNumber9.setShortcut(QCoreApplication.translate("MainWindow", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.btnNumber4.setText(QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(shortcut)
        self.btnNumber4.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.btnNumber5.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(shortcut)
        self.btnNumber5.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.btnNumber7.setText(QCoreApplication.translate("MainWindow", u"7", None))
#if QT_CONFIG(shortcut)
        self.btnNumber7.setShortcut(QCoreApplication.translate("MainWindow", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.btnNumber6.setText(QCoreApplication.translate("MainWindow", u"6", None))
#if QT_CONFIG(shortcut)
        self.btnNumber6.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.btnNumber2.setText(QCoreApplication.translate("MainWindow", u"2", None))
#if QT_CONFIG(shortcut)
        self.btnNumber2.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.btnNumber3.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(shortcut)
        self.btnNumber3.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.btnNumber0.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(shortcut)
        self.btnNumber0.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.btnComma.setText(QCoreApplication.translate("MainWindow", u".", None))
#if QT_CONFIG(shortcut)
        self.btnComma.setShortcut(QCoreApplication.translate("MainWindow", u",", None))
#endif // QT_CONFIG(shortcut)
        self.btnPlus.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(shortcut)
        self.btnPlus.setShortcut(QCoreApplication.translate("MainWindow", u"+", None))
#endif // QT_CONFIG(shortcut)
        self.btnMinus.setText(QCoreApplication.translate("MainWindow", u"-", None))
#if QT_CONFIG(shortcut)
        self.btnMinus.setShortcut(QCoreApplication.translate("MainWindow", u"-", None))
#endif // QT_CONFIG(shortcut)
        self.btnMultiply.setText(QCoreApplication.translate("MainWindow", u"x", None))
#if QT_CONFIG(shortcut)
        self.btnMultiply.setShortcut(QCoreApplication.translate("MainWindow", u"*", None))
#endif // QT_CONFIG(shortcut)
        self.btnDivide.setText(QCoreApplication.translate("MainWindow", u"/", None))
#if QT_CONFIG(shortcut)
        self.btnDivide.setShortcut(QCoreApplication.translate("MainWindow", u"/", None))
#endif // QT_CONFIG(shortcut)
        self.btnPower.setText(QCoreApplication.translate("MainWindow", u"^", None))
        self.btnEqual.setText(QCoreApplication.translate("MainWindow", u"=", None))
#if QT_CONFIG(shortcut)
        self.btnEqual.setShortcut(QCoreApplication.translate("MainWindow", u"=", None))
#endif // QT_CONFIG(shortcut)
        self.menuConfig.setTitle(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00f5es", None))
        self.menuTema.setTitle(QCoreApplication.translate("MainWindow", u"Tema", None))
    # retranslateUi

