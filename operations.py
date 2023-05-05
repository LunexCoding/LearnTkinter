from pathlib import Path
from datetime import datetime


class Operations:
    @staticmethod
    def getDate():
        current_datetime = datetime.now()
        return current_datetime.replace(microsecond=0)

    @staticmethod
    def getLst(path):
        path = Path(path)
        for item in path.glob('**/*'):
            item = Path(item)
            typeItem = "file" if item.is_file() else "dir"
            yield [item, typeItem, item.suffix]

    @staticmethod
    def createDir():
        ...

    @staticmethod
    def touch():
        ...

    @staticmethod
    def copyFile():
        ...

    @staticmethod
    def deleteTree():
        ...
