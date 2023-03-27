import sys

from PyQt5.QtWidgets import QApplication

from FernetPack.fernet import load_dotenv_data
from MessagePack import print_exception_msg
from app import MainWindow
from g_gspread import get_worksheet_by_title, get_sheet_data_by_title


def try_func(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print_exception_msg(msg=str(e))

    return wrapper


def start_app():
    marker = 'XML Parser'
    app = QApplication(sys.argv)
    app_window = MainWindow(marker=marker)
    app_window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    load_dotenv_data()
    start_app()
