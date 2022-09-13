from re import split, escape

from PySide6.QtWidgets import QMessageBox


def msg_box(titulo, texto, icone='information'):

    icons = {'information': QMessageBox.Information,
             'warning': QMessageBox.Warning,
             'critical': QMessageBox.Critical,
             'question': QMessageBox.Question}

    msg = QMessageBox()
    msg.setWindowTitle(titulo)
    msg.setText(texto)
    msg.setIcon(icons[icone])
    msg.exec()


def custom_split(separator, string):  # Split a string by a separator
    # Create a regex to split by a separator
    exp = '|'.join(map(escape, separator))
    return split(exp, string)
