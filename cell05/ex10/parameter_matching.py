#cell 5-10
import sys

if len(sys.argv) == 2:
    word = input("What was the parameter? ")
    if word == sys.argv[1] :
        print("Good job!")
    else :
        print("Nope, sory...")
else:
    print("none")