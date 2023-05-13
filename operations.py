from pathlib import Path
from datetime import datetime
from helpers.fileSystem import FileSystem
from helpers.fileSystemExceptions import (
    PathNotFoundException,
    PathExistsAsDirectoryException
)


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
        return FileSystem.makeDir(path)

    @staticmethod
    def touch(path, wipe=False):
        return FileSystem.touch(path, wipe)

    @staticmethod
    def copyFile(path, newPath, wipe=False):
        if not FileSystem.exists(path):
            print("call PathNotFoundException")
            assert PathNotFoundException(path)
        if FileSystem.exists(path) and FileSystem.isDir(path):
            assert PathExistsAsDirectoryException(path)
        return FileSystem.copyFile(path, newPath, wipe)


    @staticmethod
    def deleteTree(path):
        return FileSystem.removeTree(path)
