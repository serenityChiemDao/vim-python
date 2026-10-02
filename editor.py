
import curses

class Editor:
    def __init__(self, dataManager, view, window):
        self.dataManager = dataManager
        self.view = view
        self.window = window

    def manageInput(self):
        try:
            inputtedKey = self.window.get_wch()
            self.dataManager.actionOnInput(inputtedKey)
        except curses.error:
            pass



