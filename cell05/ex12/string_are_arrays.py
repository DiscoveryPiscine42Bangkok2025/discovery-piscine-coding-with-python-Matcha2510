#cell 5-12
import sys 
import re

if len(sys.argv) == 2 :
    scan =  re.findall(r'[z]',sys.argv[1],)
    if len(scan) != 0:
        result = "".join(scan)
        print(result)
    else:    
        print("none")
else:
    print("none")
