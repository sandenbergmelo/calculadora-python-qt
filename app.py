from PyQt5 import QtWidgets, uic
from re import split, escape
from gui.pop_up import pop_up

# Initialize the application
app = QtWidgets.QApplication([])
window = uic.loadUi('gui/ui/main.ui')

def custom_split(separator, string):# Split a string by a separator
    # Create a regex to split by a separator
    exp = '|'.join(map(escape, separator))
    return split(exp, string)

def push_number(number):# Push a number to the output

    output = window.output

    if output.text() == '0':
        output.setText('')
    
    # If last character is 0 and penultimate is an operation, delete the 0
    if len(output.text()) > 2:
        if output.text()[-1] == '0' and output.text()[-2] in '+-*/':
            delete_last_character()
    
    output.setText(output.text() + str(number))

def add_comma():# Add a comma to the output
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

def delete_last_character():# Delete the last character in the output
    window.output.setText(window.output.text()[:-1])

def operation(operation):# Add an operation to the output
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

def calculate():# Calculate the output
    output = window.output

    if output.text() == '':
        output.setText('0')
    
    # If the output ends with an operation, delete it
    if output.text()[-1] in '+-*/':
        delete_last_character()
    
    try:
        result = str(eval(output.text()))
    except ZeroDivisionError:
        pop_up('Erro', 'Impossível dividir por 0')
        result = ''

    output.setText(result)

# Events of the numbers buttons of the calculator
window.btnNumber1.clicked.connect(lambda: push_number(1))
window.btnNumber2.clicked.connect(lambda: push_number(2))
window.btnNumber3.clicked.connect(lambda: push_number(3))
window.btnNumber4.clicked.connect(lambda: push_number(4))
window.btnNumber5.clicked.connect(lambda: push_number(5))
window.btnNumber6.clicked.connect(lambda: push_number(6))
window.btnNumber7.clicked.connect(lambda: push_number(7))
window.btnNumber8.clicked.connect(lambda: push_number(8))
window.btnNumber9.clicked.connect(lambda: push_number(9))
window.btnNumber0.clicked.connect(lambda: push_number(0))

# Event of the comma button of the calculator
window.btnComma.clicked.connect(add_comma)

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

# Event of the equal button of the calculator
window.btnEqual.clicked.connect(calculate)

# Show the application
window.show()
app.exec()
