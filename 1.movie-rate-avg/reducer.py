import sys

currunt_movie_id = None
currunt_sum = 0
currunt_count = 0


for line in sys.stdin:
    line = line.strip()

    movie_id, rating = line.split('\t')

    rating = int(rating)

    if currunt_movie_id == movie_id:
        currunt_sum += rating
        currunt_count += 1
    else:
        if currunt_movie_id is not None:
            currunt_avg = currunt_sum / currunt_count
            print(f'{movie_id}\t{currunt_avg}')

        currunt_movie_id = movie_id
        currunt_sum = rating
        currunt_count = 1

if currunt_movie_id == movie_id:
    currunt_avg = currunt_sum / currunt_count
    print(f'{movie_id}\t{currunt_avg}')