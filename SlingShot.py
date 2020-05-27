# -*- coding: utf-8 -*-
"""
    SlingShot is an application that handles launching of a tester session
    in simulator mode.
    A session simulator is automatically create based on the test program.
"""
import argparse
# from LauncherCommand import LauncherCommand
import CommonMethods as util


def parseArguments():
    parser = argparse.ArgumentParser()
    # register accepted arguments for the CLI.
    parser.add_argument("--gui", help="Launch the GUI Tool",
                        action="store_true")
    parser.add_argument("-auto", help="Autoload option",
                        action="store_true")
    parser.add_argument("-l", "--load", help=".una file to load")
    args = parser.parse_args()

    # Handle user options
    if args.gui:
        print "GUI is still on development... terminating session."
        exit(1)
    if args.auto:
        print "autoload option chosen"
    if args.load:
        print(args.load)
        print(type(args.load))


if __name__ == '__main__':
    print "Program running..."
    parseArguments()
    print("Current user: ", util.getUserName())
