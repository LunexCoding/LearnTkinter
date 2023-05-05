import tkinter as tk
from tkinter import ttk, SOLID, NW, BOTH
from operations import Operations
from tkinter.simpledialog import askstring



class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.__frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8, 10])

        self.__frameExists = False

        # Buttons
        # Button Date
        self.buttonDate = ttk.Button(
            text="Show Date",
            width=20
        )
        self.buttonDate['command'] = self._showDatetime
        self.buttonDate.pack()

        # Button Lst
        self.buttonLst = ttk.Button(
            text="Show LST",
            width=20
        )
        self.buttonLst['command'] = self._buildLstTree
        self.buttonLst.pack()

        # Button Create Dir
        self.buttonCreateDir = ttk.Button(
            text="Create Dir",
            width=20
        )
        self.buttonCreateDir['command'] = Operations.createDir
        self.buttonCreateDir.pack()

        # Button Touch (create empty file)
        self.buttonTouch = ttk.Button(
            text="Touch",
            width=20
        )
        self.buttonTouch['command'] = Operations.touch
        self.buttonTouch.pack()

        # Button Copy File
        self.buttonCopyFile = ttk.Button(
            text="Copy file",
            width=20
        )
        self.buttonCopyFile['command'] = Operations.copyFile
        self.buttonCopyFile.pack()

        # Button Delete Tree
        self.buttonDeleteTree = ttk.Button(
            text="Delete Tree",
            width=20
        )
        self.buttonDeleteTree['command'] = Operations.deleteTree
        self.buttonDeleteTree.pack()

    def __setFrameExistsStatus(self, status):
        self.__frameExists = status

    def __showFrame(self):
        if not self.__frameExists:
            self.__setFrameExistsStatus(True)
            self.__frame.pack(anchor=NW, fill=BOTH, padx=5, pady=5, expand=1)

    async def __hideFrame(self):
        if self.__frameExists:
            self.__frame.pack_forget()
            self.__setFrameExistsStatus(False)

    def _showDatetime(self):
        date = Operations.getDate()
        self.__createLabel(date)

    def __openDialogInput(self, title, message):
        inputData = askstring(title, message)
        if inputData:
            return inputData

    def _buildLstTree(self):
        columns = ("#1", "#2", "#3")
        lstTree = ttk.Treeview(self.__frame, show="headings", columns=columns)
        scrollbar = ttk.Scrollbar(self.__frame, orient=tk.VERTICAL, command=lstTree.yview)
        scrollbar.grid(row=0, column=1, sticky='ns')
        lstTree.column(0, anchor="s")
        lstTree.column(1, anchor="s")
        lstTree.column(2, anchor="s")
        lstTree.grid(row=0, column=0, sticky=tk.NSEW)
        lstTree.heading("#1", text="Path")
        lstTree.heading("#2", text="Type")
        lstTree.heading("#3", text="Suffix")
        lstTree.configure(yscroll=scrollbar.set)

        path = self.__openDialogInput(
            title="LST command",
            message="Enter the path to the target folder"
        )

        items = []
        for item in Operations.getLst(path):
            items.append(item)
            lstTree.insert("", tk.END, values=item)
        self.__frameExists = True

    def __createLabel(self, text):
        if not self.__frameExists:
            self.__showFrame()
        label = tk.Label(self.__frame, text=text, font=('Aerial 18'))
        label.pack()

    def __deleteLabel(self):
        global label
        label.pack_forget()
