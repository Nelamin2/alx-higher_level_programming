#!/usr/bin/python3


def infinite_add(argv):
    argc = len(argv) - 1
    if argc == 0:
        print("{:d}".format(argc))
        return
    else:
        i = 1
        add = 0
        while i <= argc:
            add += int(argv[i])
            i += 1
        print("{:d}".format(add))


if __name__ == "__main__":
    import sys
    infinite_add(sys.argv)
