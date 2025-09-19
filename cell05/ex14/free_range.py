#cell 5-14
import sys

if len(sys.argv) == 3 :
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    nums = list(range(a,b+1))
    print(nums)
else :
    print("none")
