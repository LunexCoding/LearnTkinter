
from event import Event


class UIManager:
    onButtonShowDateClicked = Event()
    onButtonListDirClicked = Event()
    onButtonCreateDirClicked = Event()
    onButtonTouchClicked = Event()
    onButtonCopyFileClicked = Event()
    onButtonDeleteTreeClicked = Event()

    def __init__(self, window):
        self.__window = window

        self.__window.onButtonShowDateClicked += self._onButtonShowDateClicked
        self.__window.onButtonListDirClicked += self._onButtonListDirClicked
        self.__window.onButtonCreateDirClicked += self._onButtonCreateDirClicked
        self.__window.onButtonCopyFileClicked += self._onButtonCopyFileClicked
        self.__window.onButtonTouchClicked += self._onButtonTouchClicked
        self.__window.onButtonDeleteTreeClicked += self._onButtonDeleteTreeClicked

    def run(self):
        self.__window.mainloop()

    @staticmethod
    def _onButtonShowDateClicked():
        UIManager.onButtonShowDateClicked.trigger()

    @staticmethod
    def _onButtonListDirClicked(path):
        UIManager.onButtonListDirClicked.trigger(path)

    @staticmethod
    def _onButtonCreateDirClicked(path):
        UIManager.onButtonCreateDirClicked.trigger(path)

    @staticmethod
    def _onButtonCopyFileClicked(fields):
        UIManager.onButtonCopyFileClicked.trigger(fields)

    @staticmethod
    def _onButtonTouchClicked():
        UIManager.onButtonTouchClicked.trigger()


    @staticmethod
    def _onButtonDeleteTreeClicked():
        UIManager.onButtonDeleteTreeClicked.trigger()
