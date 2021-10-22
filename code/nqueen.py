#Permutations mapped to the board
'''
Permutations of 8 queens, 1 queen per row. 
Can we do better than the previous? Of course! 
If we only take care of the permutations of the numbers 1 to 8, 
and map the first place to row 1, the second place to row 2, 
and so on, we do not worry anymore about being in the same 
row or being in the same column. The total arrangements in this 
case is 8! = 40,320, 416 times better than the previous!
https://python.plainenglish.io/coding-the-8-queens-problem-in-python-d168f8df844b
'''


from itertools import permutations
import time

def print_table():
    for row in range(8):
        print(table[row])

def put_queen(x,y):
    if table[y][x] == 0:
        for m in range(8):
            table[y][m] = 1
            table[m][x] = 1
            table[y][x] = 2
            if y+m <= 7 and x+m <= 7:
                table[y+m][x+m] = 1
            if y-m >= 0 and x+m <= 7:
                table[y-m][x+m] = 1
            if y+m <= 7 and x-m >= 0:
                table[y+m][x-m] = 1
            if y-m >= 0 and x-m >= 0:
                table[y-m][x-m] = 1
        return True
    else:
        return False
start=time.perf_counter()
table = [[0]*8 for _ in range(8)]    
perms = permutations([0,1,2,3,4,5,6,7])


num_comb = 0

for perm in perms:
    if put_queen(perm[0], 0) == True:
        if put_queen(perm[1], 1) == True:
            if put_queen(perm[2], 2) == True:
                if put_queen(perm[3], 3) == True:
                    if put_queen(perm[4], 4) == True:
                        if put_queen(perm[5], 5) == True:
                            if put_queen(perm[6], 6) == True:
                                if put_queen(perm[7], 7) == True:
                                    print_table()
                                    num_comb += 1
                                    print(f"solution{num_comb}")
                                    print(" ")
    table = [[0] * 8 for _ in range(8)]
stop=time.perf_counter()
print("time = {}".format(stop-start))