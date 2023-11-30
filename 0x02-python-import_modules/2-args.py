#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arg = sys.argv
    argc = len(sys.argv) - 1
    if argc > 1:
        print("{} arguments:".format(argc))
        for i in range(1, argc + 1):
            print("{}: {}".format(i, arg[i]))

    elif argc == 0:
        print("{} arguments.".format(argc))

    else:
        print("{} argument:".format(argc))
        print("{}: {}".format(argc, arg[1]))
