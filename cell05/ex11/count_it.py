#cell 5-11
import sys

if len(sys.argv) > 1:
    print("parameters:", len(sys.argv) - 1)
    for i in range(len(sys.argv)) :
        print(f'{sys.argv[i]}: {len(sys.argv[i])}')
else:
    print("none")
