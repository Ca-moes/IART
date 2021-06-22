import numpy as np
from numpy.lib import blackman;


for j in range(0, 250):
    board1 = np.zeros((5,5), dtype=np.int8)
    for i in range(1,3):
        pieces_left = 3
        while (pieces_left > 0):
            x = np.random.randint(0, high=5, dtype=int)
            y = np.random.randint(0, high=5, dtype=int)
            if (board1[x][y] == 0):
                board1[x][y] = i
                pieces_left -= 1

    soma = 0
    for x in range(0, 5):
        for y in range(0, 5):
            if (board1[x][y] == 0):
                continue
            if (board1[x][y] == 1):
                # black pieces
                temp = (x-y)*1 
                soma += temp
                continue
            if (board1[x][y] == 2):
                # white pieces
                temp = (x-y)*2 
                soma += temp
                continue
    
    print(f'index -> {j} | value -> {soma} | board->\n{board1}')

index -> 238 | value -> 0 | board->
[[0 0 0 0 1]
 [0 2 0 0 0]
 [0 0 0 0 2]
 [2 1 0 1 0]
 [0 0 0 0 0]]

 [[0 0 0 0 2]
 [0 0 0 1 0]
 [0 0 0 0 0]
 [2 0 1 0 0]
 [0 1 0 0 2]]