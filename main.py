from PySide6.QtWidgets import QApplication

from interface.main_window import MainWindow


def main():
    app = QApplication([])
    window = MainWindow()

    app.setStyle('Fusion')
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
