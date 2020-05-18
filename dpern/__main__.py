from dpern import dpern
import sys

def main():
    args = sys.argv

    if len(args) < 2:
        error_message = "Make sure to specify a number as the first argument."
        print(error_message)
        exit(1)
    else:
        print(dpern.describe(args[1]))

if __name__ == "__main__":
    main()
