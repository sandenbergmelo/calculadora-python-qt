import json

from PySide6.QtGui import QShortcut
from PySide6.QtWidgets import QMainWindow

from interface.ui_main import Ui_MainWindow
from utils.ui_utils import msg_box, custom_split


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Calculadora')
        self.setFixedSize(self.size())

        # Read the config file
        with open('config/config.json', 'r') as config_file:
            self.configs = json.load(config_file)

        # Set the theme according to the config file
        self.change_theme(self.configs['theme'])

        ########################################
        # Connect the buttons to the functions #
        ########################################

        # Events of the numbers buttons of the calculator
        self.btnNumber0.clicked.connect(lambda: self.push_number(0))
        self.btnNumber1.clicked.connect(lambda: self.push_number(1))
        self.btnNumber2.clicked.connect(lambda: self.push_number(2))
        self.btnNumber3.clicked.connect(lambda: self.push_number(3))
        self.btnNumber4.clicked.connect(lambda: self.push_number(4))
        self.btnNumber5.clicked.connect(lambda: self.push_number(5))
        self.btnNumber6.clicked.connect(lambda: self.push_number(6))
        self.btnNumber7.clicked.connect(lambda: self.push_number(7))
        self.btnNumber8.clicked.connect(lambda: self.push_number(8))
        self.btnNumber9.clicked.connect(lambda: self.push_number(9))

        # Event of the comma button of the calculator
        self.btnComma.clicked.connect(self.add_comma)
        QShortcut('.', self, self.btnComma.click)

        # Events of the clear buttons of the calculator
        self.btnC.clicked.connect(lambda: self.output.setText(''))
        self.btnCE.clicked.connect(lambda: self.output.setText(''))

        # Event of the delete button of the calculator
        self.btnDelete.clicked.connect(self._delete_last_character)

        # Events of the operation buttons of the calculator
        self.btnPlus.clicked.connect(lambda: self.add_operation('+'))
        self.btnMinus.clicked.connect(lambda: self.add_operation('-'))
        self.btnMultiply.clicked.connect(lambda: self.add_operation('*'))
        self.btnDivide.clicked.connect(lambda: self.add_operation('/'))
        self.btnPower.clicked.connect(lambda: self.add_operation('**'))

        # Events of the equal button of the calculator
        self.btnEqual.clicked.connect(self.calculate)
        QShortcut('Return', self, self.btnEqual.click)
        QShortcut('Enter', self, self.btnEqual.click)

        # Event of the theme button of the calculator
        self.actionThemeDefault.triggered.connect(
            lambda: self.change_theme('default'))
        self.actionThemeDracula.triggered.connect(
            lambda: self.change_theme('dracula'))

    def change_theme(self, theme_name):  # Change the theme

        with open(f'config/themes/{theme_name}.css', 'r') as theme_file:
            theme = theme_file.read()
            self.setStyleSheet(theme)

        with open('config/config.json', 'w') as configs_file:
            self.configs['theme'] = theme_name
            json.dump(self.configs, configs_file, indent=4)

    def push_number(self, number):  # Push a number to the output
        if self.output.text() == '0':
            self.output.setText('')

        # If last character is 0 and penultimate is an operation, delete the 0
        if (len(self.output.text()) > 2
                and self.output.text()[-1] == '0'
                and self.output.text()[-2] in '+-*/'):
            self._delete_last_character()

        self.output.setText(self.output.text() + str(number))

    def add_comma(self):  # Add a comma to the output
        # If there is a comma in any position after an operation
        # or on the first position, do nothing
        separator = ['+', '-', '*', '/']
        string = self.output.text()
        has_comma = custom_split(separator, string)[-1].find('.')
        if has_comma != -1:
            return

        # If output is empty or the last character is an operation, add a 0
        if self.output.text() == '' or self.output.text()[-1] in '+-*/':
            self.output.setText(self.output.text() + '0')

        self.output.setText(self.output.text() + '.')

    # Delete the last character in the output
    def _delete_last_character(self):
        self.output.setText(self.output.text()[:-1])

    def add_operation(self, operation):  # Add an operation to the output

        if self.output.text() == '':
            self.output.setText('0')

        # If the last character is an operation, replace it
        if self.output.text()[-1] in '+-*/':
            self._delete_last_character()

        # If 'Calcular automaticamente' is checked, calculate the output
        if self.actionAutoCalc.isChecked() and not self.output.text().isnumeric():
            self.calculate()

        self.output.setText(self.output.text() + operation)

        # If the only character is an operation, delete it
        if self.output.text() in '+-*/' or self.output.text() == '**':
            self.output.setText('')

    def calculate(self):  # Calculate the output

        if self.output.text() == '':
            self.output.setText('0')

        # If the output ends with an operation, delete it and calculate
        if self.output.text()[-1] in '+-*/':
            self._delete_last_character()

        try:
            result = str(eval(self.output.text()))
        except ZeroDivisionError:
            msg_box('Erro', 'Impossível dividir por 0', 'critical')
            result = ''
        except Exception as err:
            print(err)
            msg_box('Erro', 'Um erro inesperado aconteceu', 'critical')
            result = ''

        # If result is larger than the maximum 16 digits, format it
        if len(result) > 16:
            result = f'{float(result):5.5}'

        self.output.setText(result)
