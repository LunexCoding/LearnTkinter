import os
from pathlib import Path
from helpers.fileSystemExceptions import (
    IsNotEmptyException,
    PathExistsException,
    PathExistsAsFileException,
    PathExistsAsDirectoryException,
    PathNotFoundException,
    IsNotDirectoryException
)
from .customExceptions import TypeException


class FileSystem:
    def __init__(self):
        pass

    @staticmethod
    def create(path, wipe=False):
        path = Path(path)
        if path.exists() and path.is_dir():
            raise PathExistsAsDirectoryException(path)
        if not isinstance(wipe, bool):
            raise TypeException("wipe", type(wipe).__name__, bool.__name__)
        path.open(mode="a").close()
        if wipe is True:
            os.truncate(str(path), 0)
        return True

    @staticmethod
    def getFilename(path, suffix=False):
        path = Path(path)
        if not path.exists():
            raise PathNotFoundException(path)
        if path.exists() and path.is_dir():
            raise PathExistsAsDirectoryException(path)
        return path.stem if suffix is False else path.name

    @staticmethod
    def listDir(path):
        return list(Path(path).glob("*"))

    @staticmethod
    def isFile(path):
        return Path(path).is_file()

    @staticmethod
    def isDir(path):
        return Path(path).is_dir()

    @staticmethod
    def isEmpty(path):
        path = Path(path)
        if not path.exists():
            raise PathNotFoundException(path)
        if not path.is_dir():
            raise IsNotDirectoryException(path)
        if not len(os.listdir(path)) == 0:
            raise IsNotEmptyException(path)
        return True

    @staticmethod
    def makeDir(path, recreate=False):
        path = Path(path)
        if path.exists() and path.is_file():
            raise PathExistsAsFileException(path)
        if path.exists() and recreate is False:
            raise PathExistsException(path)
        path.mkdir(exist_ok=recreate)
        return True

    @staticmethod
    def remove(path):
        path = Path(path)
        if not path.exists():
            raise PathNotFoundException(path)
        if path.exists() and path.is_dir():
            raise PathExistsAsDirectoryException(path)
        path.unlink()
        return True

    @classmethod
    def removeDir(cls, path):
        path = Path(path)
        if not path.exists():
            raise PathNotFoundException(path)
        if path.exists() and path.is_file():
            raise PathExistsAsFileException(path)
        if not cls.isEmpty(path):
            raise IsNotEmptyException(path)
        path.rmdir()
        return True

    @classmethod
    def removeTree(cls, path):
        path = Path(path)
        if not path.exists():
            raise PathNotFoundException(path)
        if path.exists() and path.is_file():
            raise PathExistsAsFileException(path)
        for child in path.glob("*"):
            if child.is_file():
                child.unlink()
            else:
                cls.removeTree(child)
        path.rmdir()
        return True

    @staticmethod
    def exists(path):
        return Path(path).exists()
