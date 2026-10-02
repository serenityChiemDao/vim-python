
from enumerations import Mode
import curses

class DataManager:
    def __init__(self, fileName):
        self.mode = Mode.NORMAL
        self.exit = False
        self.command = ""
        self.fileName = fileName


        try:
            file = open(self.fileName, "r")
            self.fileBuffer = []

            for line in file:
                self.fileBuffer += [line.strip("\r\n")]

            file.close()

        except FileNotFoundError:
            self.fileBuffer = []

        self.atEndOfLine = False

        if len(self.fileBuffer) == 0:
            self.cursorLine = 0
            self.cursorColumn = 0
            self.storedColumn = 0

        else:
            self.cursorLine = 1
            self.cursorColumn = len(self.fileBuffer[0])
            self.storedColumn = len(self.fileBuffer[0])


    def execute(self):
        if  self.command == ":q" or\
            self.command == ":qu" or\
            self.command == ":qui" or\
            self.command == ":quit":

            self.exit = True

        elif self.command == ":w" or\
             self.command == ":wr" or\
             self.command == ":wri" or\
             self.command == ":writ" or\
             self.command == ":write":

            file = open(self.fileName, "w")
            file.write('\n'.join(self.fileBuffer) + '\n')
            file.close()


    def actionOnInput(self, inputtedKey):
        if self.mode == Mode.NORMAL:
            if inputtedKey == 'a':
                self.cursorColumn += 1
                self.mode = Mode.INSERT
            if inputtedKey == 'i':
                self.mode = Mode.INSERT

            if inputtedKey == '0':
                self.cursorColumn = 1
                self.atEndOfLine = False

            if inputtedKey == '$':
                self.cursorColumn = len(self.fileBuffer[self.cursorLine - 1])
                self.atEndOfLine = True

            if inputtedKey == 'h':
                if self.cursorColumn > 1:
                    self.cursorColumn -= 1
                    self.storedColumn = self.cursorColumn
                    self.atEndOfLine = False

            if inputtedKey == 'l':
                if self.cursorColumn <\
                len(self.fileBuffer[self.cursorLine - 1]):
                    self.cursorColumn += 1
                    self.storedColumn = self.cursorColumn

# TODO COLUMNS!
            if inputtedKey == 'j':
                if self.cursorLine < len(self.fileBuffer):
                    self.cursorLine += 1

                if self.atEndOfLine == True:
                    self.cursorColumn =\
                    len(self.fileBuffer[self.cursorLine - 1])

                elif self.storedColumn >\
                    len(self.fileBuffer[self.cursorLine - 1]):
                        self.cursorColumn =\
                        len(self.fileBuffer[self.cursorLine - 1])

                else:
                    self.cursorColumn = self.storedColumn

            if inputtedKey == 'k':
                if self.cursorLine != 1:
                    self.cursorLine -= 1

                if self.atEndOfLine == True:
                    self.cursorColumn =\
                    len(self.fileBuffer[self.cursorLine - 1])

                elif self.storedColumn >\
                    len(self.fileBuffer[self.cursorLine - 1]):
                        self.cursorColumn =\
                        len(self.fileBuffer[self.cursorLine - 1])

                else:
                    self.cursorColumn = self.storedColumn

            elif inputtedKey == ':':
                self.mode = Mode.COMMAND
                self.command = ":"

        elif self.mode == Mode.INSERT:
            if inputtedKey == chr(27):
                self.mode = Mode.NORMAL
                if self.cursorColumn > 1:
                    self.cursorColumn -= 1
            else:
                self.fileBuffer[self.cursorLine - 1] =\
                self.fileBuffer[self.cursorLine - 1][:self.cursorColumn - 1] +\
                inputtedKey +\
                self.fileBuffer[self.cursorLine - 1][self.cursorColumn - 1:]

                self.cursorColumn += 1

        elif self.mode == Mode.COMMAND:
            if inputtedKey == chr(27):
                self.mode = Mode.NORMAL
            elif inputtedKey == chr(10):
                self.execute()
                self.mode = Mode.NORMAL
            else:
                self.command += inputtedKey


        
