#!/usr/bin/env python

with open('board.txt') as f:
    file_content = f.read()

board = []

rows = file_content.strip().split('\n')
for row in rows:
    for col in row:
        print(col)
