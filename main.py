
import curses
from curses import wrapper

import sys

from dataManager import DataManager
from view import View
from editor import Editor


def main(stdscr):
    curses.noecho()

    dataManager = DataManager(sys.argv[1])
    view = View(dataManager, stdscr)
    editor = Editor(dataManager, view, stdscr)

    while editor.dataManager.exit is False :
        editor.view.display()
        editor.manageInput()

if __name__ == '__main__':
    wrapper(main)
