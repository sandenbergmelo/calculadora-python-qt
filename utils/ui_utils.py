from re import escape, split
from typing import Any, Literal

from PySide6.QtWidgets import QMessageBox

IconType = Literal['information', 'warning', 'critical', 'question']
icons = {'information': QMessageBox.Icon.Information,
         'warning': QMessageBox.Icon.Warning,
         'critical': QMessageBox.Icon.Critical,
         'question': QMessageBox.Icon.Question}


def msg_box(title: str, txt: str, icon: IconType = 'information') -> None:
    msg = QMessageBox()
    msg.setWindowTitle(title)
    msg.setText(txt)
    msg.setIcon(icons[icon])
    msg.exec()


def replace_math_symbols(string: str):
    return string.translate(str.maketrans({'^': '**', '×': '*'}))


# Split a string by a separator
def custom_split(separators: list[str] | str, string: str) -> list[str | Any]:
    # Create a regex to split by a separator
    exp = '|'.join(map(escape, separators))
    return split(exp, string)
