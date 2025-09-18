#cell 5-9
import sys 
import re

if len(sys.argv) == 3 :
    scan =  re.findall(rf'\b{sys.argv[1]}\b',sys.argv[2])
    print(len(scan))
else:
    print("none")