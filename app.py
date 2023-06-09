from helpers.customCalendar import CustomCalendar
from uiManager import UIManager
from mainWindow import MainWindow
from operations import Operations


class App:
    def __init__(self):
        self.__window = MainWindow()
        self._ui_manager = UIManager(self.__window)

        self._ui_manager.onButtonShowDateClicked += self._onButtonShowDateClicked
        self._ui_manager.onButtonListDirClicked += self._onButtonListDirClicked
        self._ui_manager.onButtonCreateDirClicked += self._onButtonCreateDirClicked
        self._ui_manager.onButtonTouchClicked += self._onButtonTouchClicked
        self._ui_manager.onButtonCopyFileClicked += self._onButtonCopyFileClicked
        self._ui_manager.onButtonDeleteTreeClicked += self._onButtonDeleteTreeClicked

    def run(self):
        self._ui_manager.run()

    def _onButtonShowDateClicked(self):
        print("app call")
        self.__window.displayDatetime(CustomCalendar.getDatetimeNow())

    def _onButtonListDirClicked(self, path):
        print("app call")
        items = [
            ["Path", "Type", "Suffix"]
        ]
        for item in Operations.getLst(path):
            items.append(item)
        self.__window.displayFilesTable(items)

    def _onButtonCreateDirClicked(self):
        print("onButtonCreateDirClicked")

    def _onButtonTouchClicked(self):
        print("onButtonTouchClicked")

    def _onButtonCopyFileClicked(self):
        print("onButtonCopyFileClicked")

    def _onButtonDeleteTreeClicked(self):
        print("onButtonDeleteTreeClicked")
