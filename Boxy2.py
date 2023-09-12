#!/usr/bin/env python3
def your_function(n, m):
    print('*' * m)
    for i in range(n - 2):
        print('*' + (m - 2) * ' ' + '*')
    print('*' * m)
your_function(4, 5)