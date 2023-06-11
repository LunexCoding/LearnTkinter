from helpers.customCalendar import CustomCalendar
from uiManager import UIManager
from mainWindow import MainWindow
from helpers.fileSystem import FileSystem
from helpers.fileSystemExceptions import (
    IsNotEmptyException,
    PathExistsException,
    PathExistsAsFileException,
    PathExistsAsDirectoryException,
    PathNotFoundException,
    IsNotDirectoryException
)



class App:
    def __init__(self):
        self.__window = MainWindow()
        self._ui_manager = UIManager(self.__window)

        self._ui_manager.onButtonShowDateClicked += self._onButtonShowDateClicked
        self._ui_manager.onButtonListDirClicked += self._onButtonListDirClicked
        self._ui_manager.onButtonCreateDirClicked += self._onButtonCreateDirClicked
        self._ui_manager.onButtonCopyFileClicked += self._onButtonCopyFileClicked
        self._ui_manager.onButtonTouchClicked += self._onButtonTouchClicked
        self._ui_manager.onButtonDeleteTreeClicked += self._onButtonDeleteTreeClicked

    def run(self):
        self._ui_manager.run()

    def _onButtonShowDateClicked(self):
        self.__window.displayDatetime(CustomCalendar.getDatetimeNow())

    def _onButtonListDirClicked(self, path):
        items = [
            ["Path", "Type", "Suffix"]
        ]
        try:
            for item in FileSystem.listDir(path):
                items.append(item)
            self.__window.displayFilesTable(items)
        except PathNotFoundException as error:
            self.__window.showErrorMessageBox(
                title="Listing Dir",
                message=error
            )
        except PathExistsAsFileException as error:
            self.__window.showErrorMessageBox(
                title="Listing Dir",
                message=error
            )

    def _onButtonCreateDirClicked(self, path, parents=False):
        try:
            FileSystem.makeDir(path, parents)
            self.__window.showCheckmarkMessageBox(
                title="Creating Directory",
                message=f"Directory <{path}> created successfully"
            )
        except PathExistsAsFileException as error:
            self.__window.showErrorMessageBox(title="Creating Dir", message=error)
        except PathNotFoundException as error:
            response = self.__window.showWarningMessageBox(
                title="Creating Dir",
                message=f"{error}\n"
                        f"Try to recursively create a directory?",
                option_1="Cancel",
                option_2="Retry",
            )
            if response == "Retry":
                self._onButtonCreateDirClicked(path, parents=True)

    def _onButtonCopyFileClicked(self, fields):
        print(fields, "app")
        path = fields["file path"]
        newPath = fields["new file path"]
        try:
            FileSystem.copyFile(path, newPath)
            self.__window.showCheckmarkMessageBox(
                title="File Copying",
                message=f"File <{path}> copied successfully"
            )
        except PathNotFoundException as error:
            self.__window.showErrorMessageBox(
                title="File Copying",
                message=error
            )
        except PathExistsAsDirectoryException as error:
            self.__window.showErrorMessageBox(
                title="File Copying",
                message=error
            )
        except PathExistsException as error:
            self.__window.showErrorMessageBox(
                title="File Copying",
                message=error
            )

    def _onButtonTouchClicked(self):
        print("onButtonTouchClicked")

    def _onButtonDeleteTreeClicked(self):
        print("onButtonDeleteTreeClicked")
