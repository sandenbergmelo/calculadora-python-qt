import json
from pathlib import Path

from PySide6.QtGui import QShortcut
from PySide6.QtWidgets import QMainWindow

from interface.ui_main import Ui_MainWindow
from utils.ui_utils import custom_split, msg_box, replace_math_symbols


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Calculadora')
        self.setFixedSize(self.size())

        self.__operators = ['+', '-', '×', '/', '^']
        self.__parent_dir_path = Path(__file__).absolute().parent.parent
        self.__config_file_path = self.__parent_dir_path / 'config/config.json'

        # Read the config file
        with open(self.__config_file_path, 'r') as config_file:
            self.configs: dict[str, str | bool] = json.load(config_file)

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
        self.btnC.clicked.connect(lambda: self._set_output_text(''))
        self.btnCE.clicked.connect(lambda: self._set_output_text(''))

        # Event of the delete button of the calculator
        self.btnDelete.clicked.connect(self._delete_last_character)

        # Events of the operation buttons of the calculator
        self.btnPlus.clicked.connect(lambda: self.add_operator('+'))
        self.btnMinus.clicked.connect(lambda: self.add_operator('-'))
        self.btnMultiply.clicked.connect(lambda: self.add_operator('×'))
        self.btnDivide.clicked.connect(lambda: self.add_operator('/'))
        self.btnPower.clicked.connect(lambda: self.add_operator('^'))

        # Events of the equal button of the calculator
        self.btnEqual.clicked.connect(self.calculate)
        QShortcut('Return', self, self.btnEqual.click)
        QShortcut('Enter', self, self.btnEqual.click)

        # Event of the theme button of the calculator
        self.actionThemeDefault.triggered.connect(
            lambda: self.change_theme('default'))
        self.actionThemeDracula.triggered.connect(
            lambda: self.change_theme('dracula'))

    def _set_output_text(self, text: str) -> None:
        self.output.setText(text)

    def _append_text_to_output(self, text: str) -> None:
        self._set_output_text(self.output.text() + text)

    def change_theme(self, theme_name: str) -> None:
        themes_folder_path = self.__parent_dir_path / 'config/themes'
        theme_file_path = themes_folder_path / f'{theme_name}.css'

        with open(theme_file_path, 'r') as theme_file:
            theme = theme_file.read()
            self.setStyleSheet(theme)

        with open(self.__config_file_path, 'w') as config_file:
            self.configs['theme'] = theme_name
            json.dump(self.configs, config_file, indent=4)

    def push_number(self, number: int | str) -> None:
        output = self.output.text()

        # Clean the output before adding a number if the output is 0
        if output == '0':
            self._set_output_text('')

        # If last character is 0 and penultimate is an operation, delete the 0
        if (len(output) > 2 and output[-1] == '0'
                and output[-2] in self.__operators):
            self._delete_last_character()

        self._append_text_to_output(str(number))

    def add_comma(self) -> None:
        # If there is a comma in any position after an operation
        # or on the first position, do nothing
        output_txt: str = self.output.text()
        has_comma = custom_split(self.__operators, output_txt)[-1].find('.')
        if has_comma != -1:
            return

        # If output is empty or the last character is an operation, add a 0
        if output_txt == '' or output_txt[-1] in self.__operators:
            self._append_text_to_output('0')

        self._append_text_to_output('.')

    def _delete_last_character(self) -> None:
        self._set_output_text(self.output.text()[:-1])

    def add_operator(self, operation: str) -> None:

        if self.output.text() == '':
            self._set_output_text('0')

        # If the last character is an operation, replace it
        if self.output.text()[-1] in self.__operators:
            self._delete_last_character()

        # If 'Calcular automaticamente' is checked, calculate the output
        if self.actionAutoCalc.isChecked() and not self.output.text().isnumeric():
            self.calculate()

        self._append_text_to_output(operation)

        # If the only character is an operation, delete it
        if self.output.text() in self.__operators:
            self._set_output_text('')

    def calculate(self) -> None:

        if self.output.text() == '':
            self._set_output_text('0')

        # If the output ends with an operation, delete it and calculate
        if self.output.text()[-1] in self.__operators:
            self._delete_last_character()

        output_to_calc = replace_math_symbols(self.output.text())

        try:
            result = str(eval(output_to_calc))
        except ZeroDivisionError:
            msg_box('Operação inválida', 'Impossível dividir por 0', 'warning')
            result = ''
        except Exception as err:
            print(err)
            msg_box('Erro', 'Um erro inesperado aconteceu', 'critical')
            result = ''

        # If result is larger than the maximum 16 digits, format it
        if len(result) > 16:
            result = f'{float(result):5.5}'

        self._set_output_text(result)
