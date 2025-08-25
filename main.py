from stats import *
import sys

def main ():
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    else:
        report(sys.argv[1])
main()
