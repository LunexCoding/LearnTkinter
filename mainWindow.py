from customtkinter import (
    CTk,
    BOTH,
    BOTTOM,
    LEFT,
    CENTER,
    X,
    Y,
    set_appearance_mode,
    set_default_color_theme,
    CTkFont
)
from CTkMessagebox import CTkMessagebox

from event import Event
from widgets.frame import Frame
from widgets.tabView import TabView
from widgets.forms import FormWithOneFiled, FormWithTwoFields


class MainWindow(CTk):
    onButtonShowDateClicked = Event()
    onButtonListDirClicked = Event()
    onButtonCreateDirClicked = Event()
    onButtonTouchClicked = Event()
    onButtonCopyFileClicked = Event()
    onButtonDeleteTreeClicked = Event()

    def __init__(self, title="File System Operations", geometry="600x600"):
        super().__init__()
        set_appearance_mode("dark")
        set_default_color_theme("blue")
        self.title(title)
        self.geometry(geometry)
        self.minsize(500, 300)
        self._createUIEelements()

        self.__form = None
        self.__currentOperation = None

    def _createUIEelements(self):
        self.__mainFrame = self.__createFrame(self)
        self.__buttonsFrame = self.__createFrame(self.__mainFrame, fg_color="green")

        self.__showDateButton = self.__buttonsFrame.createButton('Show date', self.__onButtonShowDateClicked)
        self.__listDirButton = self.__buttonsFrame.createButton('List dir', self.__buttonListDirClicked)
        self.__createDirButton = self.__buttonsFrame.createButton('Create dir', self.__buttonCreateDirClicked)
        self.__copyFileButton = self.__buttonsFrame.createButton('Copy file', self.__buttonCopyFileClicked)
        self.__touchButton = self.__buttonsFrame.createButton('Touch file', self.__buttonTouchClicked)
        self.__deleteTreeButton = self.__buttonsFrame.createButton('Delete tree', self.__buttonDeleteTreeClicked)
        self.__showDateButton.pack(pady=[0, 20], fill=BOTH, expand=True)
        self.__listDirButton.pack(pady=[0, 20], fill=BOTH, expand=True)
        self.__createDirButton.pack(pady=[0, 20], fill=BOTH, expand=True)
        self.__copyFileButton.pack(pady=[0, 20], fill=BOTH, expand=True)
        self.__touchButton.pack(pady=[0, 20], fill=BOTH, expand=True)
        self.__deleteTreeButton.pack(pady=[0, 0], fill=BOTH, expand=True)

        self.__footerFrame = self.__createFrame(self, fg_color="blue")
        self.__copyrightLabel = self.__footerFrame.createLabel("Copyright LunexCoding",
                                                               font=CTkFont("Helvetica", 18, "bold"))
        self.__copyrightLabel.pack(side=LEFT, padx=25)

        self.__tabView = self.__createTabView(self.__mainFrame, fg_color="red")
        self.__tabView.add("Input")
        self.__tabView.add("Output")
        self.__formFrame = self.__tabView.createFrame("Input", fg_color="green")
        self.__dataFrame = self.__tabView.createFrame("Output", fg_color="green")

        self.__buttonsFrame.show(fill=Y, side=LEFT, ipadx=20)
        self.__footerFrame.show(fill=X, side=BOTTOM)
        self.__mainFrame.show(anchor=CENTER, fill=BOTH, expand=True)
        self.__tabView.show(anchor=CENTER, fill=BOTH, padx=[30, 20], pady=[0, 20], expand=True)

    @staticmethod
    def showCheckmarkMessageBox(title, message, **kwargs):
        CTkMessagebox(title=title, message=message, icon="check", **kwargs)

    @staticmethod
    def showErrorMessageBox(title, message, **kwargs):
        CTkMessagebox(title=title, message=message, icon="cancel", **kwargs)

    @staticmethod
    def showWarningMessageBox(title, message, **kwargs):
        message = CTkMessagebox(title=title, message=message, icon="warning", **kwargs)
        response = message.get()
        return response

    def __createFrame(self, master, **kwargs):
        return Frame(master, **kwargs)

    def __createTabView(self, master, **kwargs):
        return TabView(master, **kwargs)

    def __reloadFormCallbacks(self, operation):
        if self.__form is not None:
            if self.__form.name != operation:
                self.__form.clearCallbacks()

    def displayDatetime(self, datetime):
        self.__dataFrame.reload(anchor=CENTER, expand=True, fill=BOTH)
        label = self.__dataFrame.createLabel(datetime, font=CTkFont("Helvetica", 18, "bold"))
        label.show(anchor=CENTER, fill=BOTH, expand=True)
        self.__tabView.set("Output")

    def displayFilesTable(self, values):
        self.__dataFrame.reload(anchor=CENTER, fill=BOTH, expand=True)
        table = self.__dataFrame.createTable(values, hover=True)
        table.pack(anchor=CENTER, fill=BOTH, expand=True)
        self.__tabView.set("Output")

    def __buttonListDirClicked(self):
        operation = "ListDir"
        self.__formFrame.reload(anchor=CENTER, expand=True)
        self.__reloadFormCallbacks(operation)
        self.__form = FormWithOneFiled(
            master=self.__formFrame,
            name=operation,
            labelText="Enter directory path",
            placeholderText="path"
        )
        def onFormFinished(path):
            if self.__form.isValid:
                self.__onButtonListDirClicked(path)

        self.__form.onFinishEvent += onFormFinished
        self.__form.show()
        self.__tabView.set("Input")

    def __buttonCreateDirClicked(self):
        operation = "CreateDir"
        self.__formFrame.reload(anchor=CENTER, expand=True)
        self.__reloadFormCallbacks(operation)
        self.__form = FormWithOneFiled(
            master=self.__formFrame,
            name=operation,
            labelText="Enter new directory path",
            placeholderText="path"
        )
        def onFormFinished(path):
            if self.__form.isValid:
                self.__onButtonCreateDirClicked(path)

        self.__form.onFinishEvent += onFormFinished
        self.__form.show()
        self.__tabView.set("Input")

    def __buttonCopyFileClicked(self):
        operation = "CreateDir"
        self.__formFrame.reload(anchor=CENTER, expand=True)
        self.__reloadFormCallbacks(operation)
        self.__form = FormWithTwoFields(
            master=self.__formFrame,
            name=operation,
            listTextlabels=[
                "Enter copy file path",
                "Enter new file path"
            ],
            listTextPlaceholders=[
                "file path",
                "new file path"
            ]
        )
        def onFormFinished(fields):
            if self.__form.isValid:
                self.__onButtonCopyFileClicked(fields)
            self.__form.clearCallbacks()

        self.__form.onFinishEvent += onFormFinished
        self.__form.show()
        self.__tabView.set("Input")

    def __buttonTouchClicked(self):
        operation = "Touch"
        self.__formFrame.reload(anchor=CENTER, expand=True)
        self.__reloadFormCallbacks(operation)
        self.__form = FormWithOneFiled(
            master=self.__formFrame,
            name=operation,
            labelText="Enter path",
            placeholderText="path"
        )
        def onFormFinished(path):
            if self.__form.isValid:
                self.__onButtonTouchClicked(path)

        self.__form.onFinishEvent += onFormFinished
        self.__form.show()
        self.__tabView.set("Input")

    def __buttonDeleteTreeClicked(self):
        operation = "DeleteTree"
        self.__formFrame.reload(anchor=CENTER, expand=True)
        self.__reloadFormCallbacks(operation)
        self.__form = FormWithOneFiled(
            master=self.__formFrame,
            name=operation,
            labelText="Enter dir path",
            placeholderText="path"
        )

        def onFormFinished(path):
            if self.__form.isValid:
                self.__onButtonDeleteTreeClicked(path)

        self.__form.onFinishEvent += onFormFinished
        self.__form.show()
        self.__tabView.set("Input")

    @staticmethod
    def __onButtonShowDateClicked():
        MainWindow.onButtonShowDateClicked.trigger()

    @staticmethod
    def __onButtonListDirClicked(path):
        MainWindow.onButtonListDirClicked.trigger(path)

    @staticmethod
    def __onButtonCreateDirClicked(path):
        MainWindow.onButtonCreateDirClicked.trigger(path)

    @staticmethod
    def __onButtonCopyFileClicked(fields):
        MainWindow.onButtonCopyFileClicked.trigger(fields)

    @staticmethod
    def __onButtonTouchClicked(path):
        MainWindow.onButtonTouchClicked.trigger(path)

    @staticmethod
    def __onButtonDeleteTreeClicked(path):
        MainWindow.onButtonDeleteTreeClicked.trigger(path)
