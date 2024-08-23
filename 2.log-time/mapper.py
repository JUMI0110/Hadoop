import sys
import re
# re : 정규표현식 

time_pattern = re.compile(r':(\d{2}):(\d{2}):(\d{2})')

for line in sys.stdin:
    line = line.strip()
    # time = line.split(':')[1]

    match = time_pattern.search(line)

    if match:
        hour = match.group(1)
        print(f'{hour}\t1')
