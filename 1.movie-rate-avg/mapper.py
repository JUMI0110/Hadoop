import sys

for line in sys.stdin:
    line = line.strip()

    fields = line.split('\t')

    movie_id = fields[1]
    rating = fields[2]

    print(f'{movie_id}\t{rating}')