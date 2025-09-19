#cell 5-13
import sys

Word = sys.argv[1:]

if not Word:
    print("none")
else:
    for i in Word:
        match i.endswith("ism"):
            case True:
                pass
            case False:
                print(f"{i}ism")