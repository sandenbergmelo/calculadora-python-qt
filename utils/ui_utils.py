from re import escape, split

from PySide6.QtWidgets import QMessageBox


def msg_box(title, txt, icon='information'):

    icons = {'information': QMessageBox.Information,
             'warning': QMessageBox.Warning,
             'critical': QMessageBox.Critical,
             'question': QMessageBox.Question}

    msg = QMessageBox()
    msg.setWindowTitle(title)
    msg.setText(txt)
    msg.setIcon(icons[icon])
    msg.exec()


def replace_math_symbols(string: str):
    return string.replace('^', '**').replace('×', '*')


def custom_split(separator, string):  # Split a string by a separator
    # Create a regex to split by a separator
    exp = '|'.join(map(escape, separator))
    return split(exp, string)
