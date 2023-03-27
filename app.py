import os
import re
import subprocess

from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtCore import QDate, QDateTime
from colorama import Fore, Style

from AsyncProcessPack import AsyncProcess
from g_gspread import get_worksheet_by_title, get_sheet_data_by_title, create_worksheet
from save_data import save_json, get_json_data_from_file

import design
from MessagePack import print_info_msg, print_exception_msg
import xml.etree.ElementTree as Et
import numpy as np

HEADERS = {
    'дду': ["дом", "тип", "квартира", "этаж", "площадь", "text_", "ods_", "название", "документ", "дата"],
    'ипотека': ["права", "название", "документ", "дата"],
    'уступки': ["дом", "тип", "квартира", "этаж", "площадь", "text_", "ods_", "название", "документ", "дата"],
}


class MainWindow(QMainWindow, design.Ui_MainWindow):
    def __init__(self, marker: str = ''):
        # Обязательно нужно вызвать метод супер класса
        QMainWindow.__init__(self)
        self.setupUi(self)

        # ToolTips stylesheet
        self.setStyleSheet("""QToolTip {
                            border: 1px solid black;
                            padding: 3px;
                            border-radius: 3px;
                            opacity: 200;
                        }""")

        # self.ddu_list, self.i_list = [], []

        self._app_setup()
        self.setWindowTitle(marker)  # Устанавливаем заголовок окна
        self.lineEditAppEmail.setReadOnly(True)
        self.startButton.clicked.connect(self._start_click)
        self.selectFileButton.clicked.connect(self._select_file_path)
        self.clearButton.clicked.connect(self._clear_bt_click)
        self.copyButton.clicked.connect(self._copy_bt_click)
        self.lineEditStatus.setText("не запущен")
        self.results = {
            'дду': self.lineEditDduInfo,
            'ипотека': self.lineEditIpInfo,
            'уступки': self.lineEditUInfo,
        }

    def _clear_bt_click(self):
        self.lineEditUrl.setText('')
        self._save_app_setup()

    def _copy_bt_click(self):
        link = 'gorod-old-service-account@python-bot-331309.iam.gserviceaccount.com'
        self._copy2clip(link)

    @classmethod
    def _copy2clip(cls, txt):
        cmd = 'echo ' + txt.strip() + '|clip'
        return subprocess.check_call(cmd, shell=True)

    def _app_setup(self):
        if not os.path.exists('setup.json'):
            data = {
                'ss_url': '',
                'from': '01.01.2000',
                'to': '01.01.2000',
            }
            save_json(data, file_name='setup')
        setup = get_json_data_from_file('setup.json')
        self.ss_url = setup.get('ss_url')
        self.lineEditUrl.setText(self.ss_url)
        from_str = setup.get('from')
        from_ = QDate.fromString(from_str, "dd.MM.yyyy")
        self.dateEdit_from.setDate(from_)
        to_str = setup.get('to')
        to_ = QDate.fromString(to_str, "dd.MM.yyyy")
        self.dateEdit_to.setDate(to_)

    def _save_app_setup(self):
        data = {
            'ss_url': self.lineEditUrl.text(),
            'from': self.dateEdit_from.text(),
            'to': self.dateEdit_to.text()
        }
        save_json(data, file_name='setup')

    def _select_file_path(self):
        print(os.getcwd())
        path = QFileDialog.getOpenFileName(self, 'Выберите файл', os.getcwd())[0]
        self.lineEditFile.setText(path)
        print_info_msg(f'path: {path}')

    def _get_xml_file(self):
        xml_file = self.lineEditFile.text()
        if not xml_file.endswith('.xml'):
            QMessageBox.question(self, 'Внимание!', 'Расширение файла не .xml. Выберите другой файл.', QMessageBox.Ok)
            xml_file = None
        return xml_file

    @staticmethod
    def add_row_info(row, append_to, index_1=None, index_2=None):
        check = np.array(row)
        empty = True
        for cell in row:
            if cell != '':
                empty = False
                break
        if len(row) == 0 or empty:
            return
        for r in append_to:
            if np.array_equal(check, np.array(r)):
                return
        index_1 = '' if index_1 is None else Fore.BLUE + f'[{index_1}]'
        index_2 = '' if index_2 is None else Fore.BLUE + f'[{index_2}]'
        print(Fore.YELLOW + f'[PARSER]', index_1, index_2, Style.RESET_ALL + f'{row}')
        append_to.append(row)

    def _start_click(self):
        AsyncProcess("status", self._set_status, 1, (self, "_pars_data"))

    def _pars_data(self):
        self.ddu_list, self.i_list, self.u_list = [], [], []
        # check file path
        xml_file = self._get_xml_file()
        if xml_file is None:
            self.lineEditStatus.setText('не запущен')
            return
        self._save_app_setup()
        self.ss_url = self.lineEditUrl.text()
        start_date = self.dateEdit_from.date()
        end_date = self.dateEdit_to.date()
        # create element tree object
        tree = Et.parse(xml_file)
        print(tree)

        # get root element
        root = tree.getroot()
        print(root)

        els = root.findall('./deal_records/deal_record')
        print(len(els))

        for el in els:
            house_, type_, flat_, floor_, area_, text_, ods_, doc_, date_, name_ = \
                '', '', '', '', '', '', '', '', '', ''
            try:
                doc_ = el.findall('./underlying_documents/underlying_document/document_number')[0].text
            except Exception as e:
                # print_exception_msg(str(e))
                pass
            if '/п' not in doc_.lower() and '-нп' not in doc_.lower() and '-п' not in doc_.lower():
                doc_date = None
                try:
                    date_ = el.findall('./underlying_documents/underlying_document/document_date')[0].text
                    y, m, d = date_.split('-')
                    doc_date = QDate(int(y), int(m), int(d))
                    # date_ = datetime(int(y), int(m), int(d))
                    date_ = f"{int(d)}.{int(m)}.{int(y)}"
                except Exception as e:
                    # print_exception_msg('date_, ' + str(e))
                    pass
                # print(start_date.toPyDate(), doc_date.toPyDate(), end_date.toPyDate())
                if doc_date and start_date <= doc_date <= end_date:
                    try:
                        name_ = el.findall('./underlying_documents/underlying_document/document_name')[0].text
                    except Exception as e:
                        # print_exception_msg('name_, ' + str(e))
                        pass
                    try:
                        house_ = el.findall('./deal_data/subject/share_subject_description/house_descriptions'
                                            '/house_description/house_number')[0].text
                    except Exception as e:
                        # print_exception_msg('house_, ' + str(e))
                        pass
                    try:
                        type_ = el.findall('./deal_data/subject/share_subject_description/house_descriptions'
                                           '/house_description/room_descriptions/room_description/room_name')[0].text
                    except Exception as e:
                        # print_exception_msg('type_, ' + str(e))
                        pass
                    try:
                        flat_ = el.findall('./deal_data/subject/share_subject_description/house_descriptions'
                                           '/house_description/room_descriptions/room_description/room_number')[0].text
                    except Exception as e:
                        # print_exception_msg('flat_, ' + str(e))
                        pass
                    try:
                        floor_ = el.findall('./deal_data/subject/share_subject_description/house_descriptions'
                                            '/house_description/room_descriptions/room_description/floor_number')[
                            0].text
                    except Exception as e:
                        # print_exception_msg('floor_, ' + str(e))
                        pass
                    try:
                        area_ = el.findall('./deal_data/subject/share_subject_description/house_descriptions'
                                           '/house_description/room_descriptions/room_description/room_area')[0].text
                    except Exception as e:
                        # print_exception_msg('area_, ' + str(e))
                        pass
                    try:
                        text_ = el.findall('./deal_data/subject/share_subject_description/house_descriptions'
                                           '/house_description/room_descriptions/room_description/text_description')
                        if len(text_) > 0:
                            text_ = text_[0].text
                        else:
                            text_ = ''
                    except Exception as e:
                        # print_exception_msg('text_, ' + str(e))
                        pass
                    try:
                        ods_ = el.findall('./deal_data/subject/share_subject_description/ods_description')[0].text
                    except Exception as e:
                        # print_exception_msg('ods_, ' + str(e))
                        pass
                    row = [house_, type_, flat_, floor_, area_, text_, ods_, name_, doc_, date_]
                    if "уступки прав" in name_.lower():
                        self.add_row_info(row, self.u_list, 'ust')
                    else:
                        self.add_row_info(row, self.ddu_list, 'ddu')

        els = root.findall('./restrict_records/restrict_record')
        print(len(els))

        for el in els:
            doc_, date_, name_, right_ = '', '', '', ''
            doc_date = None
            try:
                date_ = el.findall('./underlying_documents/underlying_document/document_date')[0].text
                y, m, d = date_.split('-')
                doc_date = QDate(int(y), int(m), int(d))
                # date_ = datetime(int(y), int(m), int(d))
                date_ = f"{int(d)}.{int(m)}.{int(y)}"
            except Exception as e:
                # print_exception_msg('date_, ' + str(e))
                pass
            if doc_date and start_date <= doc_date <= end_date:
                try:
                    doc_ = el.findall('./underlying_documents/underlying_document/document_number')[0].text
                except Exception as e:
                    # print_exception_msg('doc_, ' + str(e))
                    pass
                try:
                    name_ = el.findall('./underlying_documents/underlying_document/document_name')[0].text
                except Exception as e:
                    # print_exception_msg('name_, ' + str(e))
                    pass
                try:
                    right_ = el.findall('./right_holders/right_holder/legal_entity/entity/resident/name')[0].text
                except Exception as e:
                    # print_exception_msg('right_, ' + str(e))
                    pass

                row = [right_, name_, doc_, date_]
                self.add_row_info(row, self.i_list, 'ipt')

        data = {
            'дду': self.ddu_list,
            'ипотека': self.i_list,
            'уступки': self.u_list,
        }
        self.insert_sheet_data(data)
        self.lineEditStatus.setText('не запущен')

    def insert_sheet_data(self, data):
        for key, new_data in data.items():
            if len(new_data) > 0:
                # get current sheet data
                worksheet, sheet_data = self.get_sheet_data(key, new_data)
                # check duplicate rows
                if len(sheet_data) > 0:
                    new_data = self.np_check(new_data, sheet_data)
                self.results[key].setText(f"+{len(new_data)}")
                new_data.extend(sheet_data)
                new_data.insert(0, HEADERS[key])
                print_info_msg(f"new data count: {len(new_data)}")
                self.update_sheet_data(worksheet, new_data)

    @classmethod
    def update_sheet_data(cls, worksheet, new_data):
        try:
            worksheet.clear()
            worksheet.update('A1', new_data)
        except Exception as e:
            print_exception_msg(f"{str(e)}")

    def get_sheet_data(self, name, tab_data):
        worksheet, sheet_data = None, None
        ss_id = self.get_id_from_url(self.ss_url)
        try:
            sheet_data = get_sheet_data_by_title(ss_id, name)
        except Exception as e:
            # print_exception_msg(f"{str(e)}")
            pass
        count = len(sheet_data) if sheet_data else 0
        print_info_msg(f"tab: {name}, row count: {count}")
        try:
            if sheet_data is None:
                # worksheet = create_worksheet(ss_id, name, rows=1000, cols=len(tab_data[0]))
                worksheet = create_worksheet(ss_id, name, rows=10, cols=len(tab_data[0]))
            else:
                if len(sheet_data) > 0 and np.array_equal(np.array(sheet_data[0]), np.array(HEADERS[name])):
                    sheet_data = sheet_data[1:]
                worksheet = get_worksheet_by_title(ss_id, name)
        except Exception as e:
            # print_exception_msg(f"{str(e)}")
            pass
        if sheet_data is None:
            sheet_data = []
        return worksheet, sheet_data

    @classmethod
    def np_check(cls, new_data, data):
        checked = []
        for new in new_data:
            new_ = np.array(new)
            equal = False
            for row in data:
                if np.array_equal(new_, np.array(row)):
                    equal = True
                    break
            if not equal:
                checked.append(new)
        return checked

    @classmethod
    def get_id_from_url(cls, url):
        matches = re.findall(r"[-\w]{25,}", url)
        uid = matches[0]
        return uid

    def _set_status(self):
        for key, result in self.results.items():
            result.setText("0")
        self.lineEditStatus.setText('запущен')