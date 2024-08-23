import sys

last_word = None
total_count = 0

for line in sys.stdin:
    line = line.strip()


    word, value = line.split('\t')
    value = int(value)

    
    if last_word == word:
        total_count += value
    
    else:
        if last_word is not None:
            print(f'{last_word}\t{total_count}')
        total_count = value
        last_word = word


if last_word == word:
    print(f'{last_word}\t{total_count}')
