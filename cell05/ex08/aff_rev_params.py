#cell 5-8
import sys
args = sys.argv[1:]
if len(sys.argv) > 2:
    for i in reversed(args) : 
        print(i)
else:
    print("none")