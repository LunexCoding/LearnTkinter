
from event import Event


class UIManager:
    # атрибуты класса, были в конструкторе
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
        self.__window.onButtonTouchClicked += self._onButtonTouchClicked
        self.__window.onButtonCopyFileClicked += self._onButtonCopyFileClicked
        self.__window.onButtonDeleteTreeClicked += self._onButtonDeleteTreeClicked

    def run(self):
        self.__window.mainloop()

    @staticmethod
    def _onButtonShowDateClicked():
        print("UI call")
        UIManager.onButtonShowDateClicked.trigger()

    @staticmethod
    def _onButtonListDirClicked():
        print("UI call")
        UIManager.onButtonListDirClicked.trigger()

    def _onButtonCreateDirClicked(self):
        UIManager.onButtonCreateDirClicked.trigger()

    def _onButtonTouchClicked(self):
        self.onButtonTouchClicked.trigger()

    def _onButtonCopyFileClicked(self):
        self.onButtonCopyFileClicked.trigger()

    def _onButtonDeleteTreeClicked(self):
        self.onButtonDeleteTreeClicked.trigger()
