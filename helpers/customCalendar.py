from datetime import datetime


class CustomCalendar:
    @staticmethod
    def getDatetimeNow():
        return datetime.today().replace(microsecond=0)
