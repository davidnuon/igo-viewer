#!/usr/bin/env python

with open('board.txt') as f:
    file_content = f.read()

board = []

BLACK = '⚫ '
WHITE = '⚪ '
BLANK = '☩ '

rows = file_content.strip().split('\n')
for row in rows:
    printed_row = ''
    for col in row:
        if col == '.':
            printed_row += BLANK
        elif col == 'X':
            printed_row += BLACK
        elif col == '0':
            printed_row += WHITE
    print(printed_row)
