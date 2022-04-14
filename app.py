import json
from re import split, escape
from PyQt5 import QtWidgets, uic
from gui.pop_up import pop_up


# Initialize the application
app = QtWidgets.QApplication([])
window = uic.loadUi('gui/ui/main.ui')

app.setStyle('Fusion')

# Read the config file
with open('config.json', 'r') as config_file:
    configs = json.load(config_file)

def change_theme(theme_name):  # Change the theme

    with open(f'themes/{theme_name}.css', 'r') as theme_file:
        theme = theme_file.read()
        window.setStyleSheet(theme)

    with open('config.json', 'w') as configs_file:
        configs['theme'] = theme_name
        json.dump(configs, configs_file, indent=4)

# Set the theme according to the config file
change_theme(configs['theme'])

def custom_split(separator, string):  # Split a string by a separator
    # Create a regex to split by a separator
    exp = '|'.join(map(escape, separator))
    return split(exp, string)


def push_number(number):  # Push a number to the output
    output = window.output

    if output.text() == '0':
        output.setText('')

    # If last character is 0 and penultimate is an operation, delete the 0
    if (len(output.text()) > 2
            and output.text()[-1] == '0'
            and output.text()[-2] in '+-*/'):
        delete_last_character()

    output.setText(output.text() + str(number))


def add_comma():  # Add a comma to the output
    output = window.output

    # If there is a comma in any position after an operation
    # or on the first position, do nothing
    separator = ['+', '-', '*', '/']
    after_an_operation = custom_split(separator, output.text())[-1].find('.')
    if after_an_operation != -1:
        return

    # If output is empty or the last character is an operation, add a 0
    if output.text() == '' or output.text()[-1] in '+-*/':
        output.setText(output.text() + '0')

    output.setText(output.text() + '.')


def delete_last_character():  # Delete the last character in the output
    window.output.setText(window.output.text()[:-1])


def operation(operation):  # Add an operation to the output
    output = window.output

    if output.text() == '':
        output.setText('0')

    # If the last character is an operation, replace it
    if output.text()[-1] in '+-*/':
        delete_last_character()

    # If 'Calcular automaticamente' is checked, calculate the output
    if window.actionAutoCalc.isChecked() and not output.text().isnumeric():
        calculate()

    output.setText(output.text() + operation)

    # If the only character is an operation, delete it
    if output.text() in '+-*/' or output.text() == '**':
        output.setText('')


def calculate():  # Calculate the output
    output = window.output

    if output.text() == '':
        output.setText('0')

    # If the output ends with an operation, delete it and calculate
    if output.text()[-1] in '+-*/':
        delete_last_character()

    try:
        result = str(eval(output.text()))
    except ZeroDivisionError:
        pop_up('Erro', 'Impossível dividir por 0')
        result = ''
    except:
        pop_up('Erro', 'Um erro inesperado aconteceu')
        result = ''

    # If result is larger than the maximum 16 digits, format it
    if len(result) > 16:
        result = f'{float(result):5.5}'

    output.setText(result)


for i in range(10):  # Events of the numbers buttons of the calculator
    exec(f'window.btnNumber{i}.clicked.connect(lambda: push_number({i}))')

# Event of the comma button of the calculator
window.btnComma.clicked.connect(add_comma)
QtWidgets.QShortcut('.', window, window.btnComma.click)

# Events of the clear buttons of the calculator
window.btnC.clicked.connect(lambda: window.output.setText(''))
window.btnCE.clicked.connect(lambda: window.output.setText(''))

# Event of the delete button of the calculator
window.btnDelete.clicked.connect(delete_last_character)

# Events of the operation buttons of the calculator
window.btnPlus.clicked.connect(lambda: operation('+'))
window.btnMinus.clicked.connect(lambda: operation('-'))
window.btnMultiply.clicked.connect(lambda: operation('*'))
window.btnDivide.clicked.connect(lambda: operation('/'))
window.btnPower.clicked.connect(lambda: operation('**'))

# Events of the equal button of the calculator
window.btnEqual.clicked.connect(calculate)
QtWidgets.QShortcut('Return', window, window.btnEqual.click)
QtWidgets.QShortcut('Enter', window, window.btnEqual.click)

# Event of the theme button of the calculator
window.actionThemeDefault.triggered.connect(lambda: change_theme('default'))
window.actionThemeDracula.triggered.connect(lambda: change_theme('dracula'))

# Show the application
window.show()
app.exec()
