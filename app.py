from uiManager import UIManager
from dbManager import DBManager


class App:
    def __init__(self):
        self.__ui_manager = UIManager()

        # Регистрируем колбэки UIManager в DBManager
        self.__ui_manager.onButtonShowDateClicked(self._onButtonShowDateClicked)
        self.__ui_manager.onButtonListDirClicked(self._onButtonListDirClicked)
        self.__ui_manager.onButtonCreateDirClicked(self._onButtonCreateDirClicked)
        self.__ui_manager.onButtonTouchClicked(self._onButtonTouchClicked)
        self.__ui_manager.onButtonCopyFileClicked(self._onButtonCopyFileClicked)
        self.__ui_manager.onButtonDeleteTreeClicked(self._onButtonDeleteTreeClicked)

    def run(self):
        self.__ui_manager.run()

    def _onButtonShowDateClicked(self):
        print("onButtonShowDateClicked")

    def _onButtonListDirClicked(self):
        print("onButtonListDirClicked")

    def _onButtonCreateDirClicked(self):
        print("onButtonCreateDirClicked")

    def _onButtonTouchClicked(self):
        print("onButtonTouchClicked")

    def _onButtonCopyFileClicked(self):
        print("onButtonCopyFileClicked")

    def _onButtonDeleteTreeClicked(self):
        print("onButtonDeleteTreeClicked")
