import random
import shutil
import sys
import time

#  DA MATRIX

#  set up constants
min_stream_length = 50
max_stream_length = 100
pause = 0.1
stream_chars = [' \U0000264A',' \U000131F3', ' \U00001F68',' \U0000262D', ' \U000026EC',' \U00002629', ' \U00002665' ]

#  density can range from 0.0 to 1.0
density = 0.02

width = shutil.get_terminal_size()[0]
#  can't print to the last column on Windows without adding a
#  newline automatically, so reduce the width by one
width -= 1

print('Press CTRL+C to quit')
time.sleep(2)

try:
    columns = [0] * width
    while True:
        for i in range(width):
            if columns[i] == 0:
                if random.random() <= density:
                    columns[i] = random.randint(min_stream_length,
                                                max_stream_length)
                    
            if columns[i] > 0:
                print(random.choice(stream_chars), end='')
                columns[i] -= 1
            else:
                print(' ',end='')
        print()
        sys.stdout.flush()
        time.sleep(pause)
except KeyboardInterrupt:
    sys.exit()
