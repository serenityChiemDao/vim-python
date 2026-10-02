
from enumerations import Mode
import curses

class View:
    def __init__(self, dataManager, window):
        self.dataManager = dataManager
        self.window = window

    def display(self):
        emptyLine = (curses.COLS - 1) * ' '

        l = 0

        for line in self.dataManager.fileBuffer:
            self.window.addstr(l, 0, self.dataManager.fileBuffer[l])
            l += 1

        if self.dataManager.mode == Mode.NORMAL:
            self.window.addstr(curses.LINES - 1, 0, emptyLine)
            self.window.move(0, 0)

        elif self.dataManager.mode == Mode.COMMAND:
            self.window.addstr(curses.LINES - 1, 0, emptyLine)
            self.window.addstr(curses.LINES - 1, 0, self.dataManager.command)

        elif self.dataManager.mode == Mode.INSERT:
            self.window.addstr(curses.LINES - 1, 0, emptyLine)
            self.window.addstr(curses.LINES - 1, 0, "-- INSERT --")

        self.window.addstr(curses.LINES - 1, curses.COLS - 15,
                           str(self.dataManager.cursorLine) + "," +
                           str(self.dataManager.cursorColumn))

        if self.dataManager.cursorLine - 1 >= 0:
            y = self.dataManager.cursorLine - 1
        else:
            y = 0

        if self.dataManager.cursorColumn - 1 >= 0:
            x = self.dataManager.cursorColumn - 1
        else:
            x = 0


        self.window.move(y, x)

