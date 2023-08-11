# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

from curses import wrapper

def main(stdscr):
    stdscr.clear()
    stdscr.addstr(10,25, "hello world")
    stdscr.refresh()
    stdscr.getch()

wrapper(main)



