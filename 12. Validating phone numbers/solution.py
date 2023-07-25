import re

for _ in range(int(input())):
    print(['NO', 'YES'][bool(re.match(r'^[789]\d{9}$', input()))])