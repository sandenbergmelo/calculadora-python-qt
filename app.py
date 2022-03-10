from PyQt5 import QtWidgets, uic

# Initialize the application
app = QtWidgets.QApplication([])
window = uic.loadUi('gui/ui/main.ui')

def push_number(number): # Push a number to the output
    output = window.output
    output.setText(output.text() + str(number))

def add_comma():# Add a comma to the output
    output = window.output
    
    # If there is already a comma, do nothing
    if '.' in output.text():
        return
    if output.text() == '':
        output.setText('0')
    
    output.setText(output.text() + '.')

def delete_last_character(): # Delete the last character in the output
    window.output.setText(window.output.text()[:-1])

def operation(operation):# Add an operation to the output
    output = window.output

    # If the last character is an operation, replace it
    if output.text()[-1] in '+-*/':
        delete_last_character()
    if output.text() == '':
        output.setText('0')
    
    output.setText(output.text() + operation)

def calculate(): # Calculate the output
    output = window.output

    if output.text() == '':
        output.setText('0')
    # If the output ends with an operation, delete it
    if output.text()[-1] in '+-*/':
        delete_last_character()
    result = str(eval(output.text()))
    output.setText(result)

# Event of the numbers buttons of the calculator
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

# Event of the clear buttons of the calculator
window.btnC.clicked.connect(lambda: window.output.setText(''))
window.btnCE.clicked.connect(lambda: window.output.setText(''))

# Event of the delete button of the calculator
window.btnDelete.clicked.connect(delete_last_character)

# Event of the operation buttons of the calculator
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
