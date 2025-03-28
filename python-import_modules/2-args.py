#!/usr/bin/python3
import sys

if __name__ == "__main__":

    argv = sys.argv[1:]
    argc = len(argv)

    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
        print("{}: {}".format(argc, argv[0]))
    elif argc > 1:
        print("{} arguments:".format(argc))

        for i, arg in enumerate(argv, start=0):
            print("{}: {}".format(i, arg))
