from pathlib import Path
from datetime import datetime
from helpers.fileSystem import FileSystem


class Operations:
    @staticmethod
    def getDate():
        current_datetime = datetime.now()
        return current_datetime.replace(microsecond=0)

    @staticmethod
    def getLst(path):
        path = Path(path)
        return FileSystem.listDir(path)

    @staticmethod
    def createDir(path):
        Path(path).mkdir()

    @staticmethod
    def touch():
        ...

    @staticmethod
    def copyFile():
        ...

    @staticmethod
    def deleteTree():
        ...
