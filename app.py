import tkinter as tk
from tkinter import ttk, SOLID, NW, BOTH
from tkinter.simpledialog import askstring
from tkinter import messagebox

from operations import Operations
from helpers.fileSystem import FileSystem
from helpers.fileSystemExceptions import (
    PathExistsAsDirectoryException,
    PathExistsException,
    PathNotFoundException
)


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
        self.buttonCreateDir['command'] = self._createDir
        self.buttonCreateDir.pack()

        # Button Touch (create empty file)
        self.buttonTouch = ttk.Button(
            text="Touch",
            width=20
        )
        self.buttonTouch['command'] = self._touch
        self.buttonTouch.pack()

        # Button Copy File
        self.buttonCopyFile = ttk.Button(
            text="Copy file",
            width=20
        )
        self.buttonCopyFile['command'] = self._copyFile
        self.buttonCopyFile.pack()

        # Button Delete Tree
        self.buttonDeleteTree = ttk.Button(
            text="Delete Tree",
            width=20
        )
        self.buttonDeleteTree['command'] = self._deleteTree
        self.buttonDeleteTree.pack()

    def __setFrameExistsStatus(self, status):
        self.__frameExists = status

    def __createFrame(self):
        if not self.__frameExists:
            self.__frame.pack(anchor=NW, fill=BOTH, padx=5, pady=5, expand=1)
            self.__setFrameExistsStatus(True)

    def __destroyFrame(self):
        if self.__frameExists:
            for widget in self.__frame.winfo_children():
                widget.destroy()
            self.__setFrameExistsStatus(False)

    def __openDialogInput(self, title, message):
        inputData = askstring(title, message)
        if inputData:
            return inputData
        return

    def __reloadFrame(self):
        if self.__frameExists:
            self.__destroyFrame()
        if not self.__frameExists:
            self.__createFrame()

    def __createLabel(self, text):
        self.__reloadFrame()
        label = tk.Label(self.__frame, text=text, font=('Aerial 18'))
        label.pack()

    def _showDatetime(self):
        date = Operations.getDate()
        self.__createLabel(date)

    def _buildLstTree(self):
        self.__reloadFrame()
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

        path = self.__openDialogInput(
            title="LST command",
            message="Enter the path to the target folder"
        )
        if path:
            items = []
            for item in Operations.getLst(path):
                items.append(item)
                lstTree.insert("", tk.END, values=item)

    def _createDir(self):
        path = self.__openDialogInput(
            title="Creating Directory",
            message="Input path for new directory"
        )
        if path:
            try:
                Operations.createDir(path)
            except PathExistsException:
                messagebox.showwarning(
                    title="Creating Directory",
                    message=F"Directory with name <{path}> already exists"
                )

    def _touch(self):
        path = self.__openDialogInput(
            title="Creating Directory",
            message="Input path for new directory"
        )
        if path:
            try:
                Operations.touch(path)
            except PathExistsException:
                wipe = messagebox.askyesno(
                    title="Touching file",
                    message=F"File with name <{path}> already exists.\nOverwrite file?"
                )
                if wipe:
                    Operations.touch(path, wipe)
            except PathExistsAsDirectoryException:
                messagebox.showerror(
                    title="Touching file",
                    message=F"File with name <{path}> already exists as directory."
                )

    def _copyFile(self):
        path = self.__openDialogInput(
            title="Copy File",
            message="Input path for file to copy"
        )
        if path:
            try:
                if not FileSystem.exists(path):
                    raise PathNotFoundException(path)
                if FileSystem.exists(path) and FileSystem.isDir(path):
                    raise PathExistsAsDirectoryException(path)
                newPath = self.__openDialogInput(
                    title="Copy File",
                    message="Input path for copy file"
                )
                if newPath:
                    try:
                        if FileSystem.exists(newPath) and FileSystem.isDir(newPath):
                            raise PathExistsAsDirectoryException(newPath)
                        if FileSystem.exists(newPath):
                            raise PathExistsException(newPath)
                        Operations.copyFile(path, newPath)
                    except PathExistsAsDirectoryException:
                        messagebox.showerror(
                            title="Copy File",
                            message=F"File with name <{newPath}> already exists as directory."
                        )
                    except PathExistsException:
                        wipe = messagebox.askyesno(
                            title="Copy File",
                            message=F"File with name <{newPath}> already exists.\nOverwrite file?"
                        )
                        if wipe:
                            Operations.copyFile(path, newPath, wipe)
            except PathNotFoundException:
                print("PathNotFoundException")
                messagebox.showerror(
                    title="Copy File",
                    message=F"File with name <{path}> not found."
                )
            except PathExistsAsDirectoryException:
                print("PathExistsAsDirectoryException")
                messagebox.showerror(
                    title="Copy File",
                    message=F"File with name <{path}> already exists as directory."
                )

    def _deleteTree(self):
        path = self.__openDialogInput(
            title="Delete Tree",
            message="Input path for deleting Tree"
        )
        if path:
            Operations.deleteTree(path)
