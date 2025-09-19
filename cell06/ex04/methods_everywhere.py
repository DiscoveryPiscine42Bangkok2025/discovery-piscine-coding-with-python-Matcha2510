#cell 6-4
import sys

if len(sys.argv) <= 1:
    print("none")
else:
    for i, val in enumerate(sys.argv[1:]):
        if (len(val) <= 1):
            print("none")
        elif (len(val) < 8):
            print(val, end='')
            for i in range(8 - len(val)):
                print("Z", end='')
        else:
            print(f"{val}")