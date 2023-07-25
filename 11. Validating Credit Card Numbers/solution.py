import re
from itertools import groupby

pattern = r"^[456]\d{3}-?(\d{4}-?){2}\d{4}$"
for _ in range(int(input())):
    valid = True
    S = input()
    if re.match(pattern, S):
        for k, v in groupby(S.replace('-', '')):
            if len(list(v)) > 3:
                print("Invalid")
                valid = False
                break
        if valid:
            print("Valid")
    else:
        print("Invalid")