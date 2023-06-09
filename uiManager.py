from tkinter import Tk
from mainWindow import MainWindow
from event import Event


class UIManager:
    def __init__(self):
        self.__window = MainWindow()

        # Создаем события
        self.onButtonShowDateClicked = Event()
        self.onButtonListDirClicked = Event()
        self.onButtonCreateDirClicked = Event()
        self.onButtonTouchClicked = Event()
        self.onButtonCopyFileClicked = Event()
        self.onButtonDeleteTreeClicked = Event()

        # Подписываемся на события окна
        self.__window.onButtonShowDateClicked += self._onButtonShowDateClicked
        self.__window.onButtonListDirClicked += self._onButtonListDirClicked
        self.__window.onButtonCreateDirClicked += self._onButtonCreateDirClicked
        self.__window.onButtonTouchClicked += self._onButtonTouchClicked
        self.__window.onButtonCopyFileClicked += self._onButtonCopyFileClicked
        self.__window.onButtonDeleteTreeClicked += self._onButtonDeleteTreeClicked

    def run(self):
        self.__window.mainloop()

    def _onButtonShowDateClicked(self):
        self.onButtonShowDateClicked.trigger()

    def _onButtonListDirClicked(self):
        self.onButtonListDirClicked.trigger()

    def _onButtonCreateDirClicked(self):
        self.onButtonCreateDirClicked.trigger()

    def _onButtonTouchClicked(self):
        self.onButtonTouchClicked.trigger()

    def _onButtonCopyFileClicked(self):
        self.onButtonCopyFileClicked.trigger()

    def _onButtonDeleteTreeClicked(self):
        self.onButtonDeleteTreeClicked.trigger()
