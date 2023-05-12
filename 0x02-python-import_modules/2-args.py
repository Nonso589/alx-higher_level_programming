#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argu = len(sys.argv) - 1
    if argu == 0:
        print("0 arguments.")
    elif argu == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argu))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
