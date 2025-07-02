import openpyxl
import pyperclip
import time

cell_row = 2
_column = 2
clipboard_previous_value = pyperclip.paste()
clipboard_value = pyperclip.paste()

_workbook = openpyxl.open("games.xlsx")
_worksheet = _workbook.worksheets[0]

try:
    while True:
        clipboard_value = pyperclip.paste()
        
        if clipboard_value != clipboard_previous_value:
            print(clipboard_value)
            _worksheet.cell(cell_row, _column).value = clipboard_value
            clipboard_previous_value = clipboard_value
            cell_row += 1
        time.sleep(1)
except KeyboardInterrupt:

    _workbook.save("games.xlsx")
