import openpyxl
import datetime


class WorkTable:
    def get_date(self, message):
        user_id = message.chat.id
        date = datetime.date.today()
        book = openpyxl.open(f"{user_id}.xlsx", read_only=False)
        sheet = book.active
        for row in range(2, sheet.max_row + 1):
            if sheet[1][row].value is None:
                sheet[1][row].value = date
        book.save(f"{user_id}.xlsx")
        book.close()
