import sys

last_hour = None
total_count = 0

for line in sys.stdin:
    line = line.strip()


    hour, value = line.split('\t')
    value = int(value)

    
    if last_hour == hour:
        total_count += value
    
    else:
        if last_hour is not None:
            print(f'{last_hour}\t{total_count}')
        total_count = value
        last_hour = hour


if last_hour == hour:
    print(f'{last_hour}\t{total_count}')



