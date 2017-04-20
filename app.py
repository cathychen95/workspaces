from subprocess import call, Popen, PIPE
import sys
from sys_commands import *

# https://github.com/rrg/ListOpenFiles/blob/master/listopenfiles.py

program_extensions = {
    "Pages": [
        ".pages"
    ],
    "Preview": [
        ".pdf"  # exclude things after /Applications
    ]
}

# Pages
# Word
# Excel
# Powerpoint
# Preview
# Adobe
# Chrome <-
# Safari
# Firefox


w_store = {
    "coding_hw": [
        "test.py",
        "https://www.tutorialspoint.com/python/python_dictionary.htm"
    ]
}


def save_workspace(workspace):
    # Chrome

    windows = Popen(
        sys_commands["chrome"][0],
        shell=True,
        stdout=PIPE
    ).communicate()[0]
    if int(windows):
        print windows.strip() + " windows"
    else:
        print "no windows open"


def open_workspaces(workspaces):
    for workspace in workspaces:
        if workspace in w_store:
            for file in w_store[workspace]:
                call(["open", file])
        else:
            print "Workspace doesn't exist."


def show_workspaces():
    pass


def main(argv):
    if len(argv):
        if argv[0] == "save":
            if len(argv[1:]):
                save_workspace(argv[1:])
            else:
                print "error"
        elif argv[0] == "open":
            if len(argv[1:]):
                open_workspaces(argv[1:])
            else:
                print "error"
        elif argv[0] == "workspaces":
            show_workspaces()

    else:
        print "No arguments"


if __name__ == "__main__":
    main(sys.argv[1:])
