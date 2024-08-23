import sys

# sys.stdin : system standardinput
for line in sys.stdin:
    line = line.strip() # strip 좌우공백 제거
    words = line.split() # split 인자 넣지 않으면 뛰어쓰기를 기준으로 분리

    for word in words:
        print(f'{word}\t1') # \t 들여쓰기