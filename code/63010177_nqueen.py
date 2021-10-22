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
print("Iterative")
for i in range(7):
  N=i+4
  def print_table():
      for row in range(N):
          print(table[row])

  def put_queen(x,y):
      if table[y][x] == 0:
          for m in range(N):
              table[y][m] = 1
              table[m][x] = 1
              table[y][x] = 2
              if y+m <= N-1 and x+m <= N-1:
                  table[y+m][x+m] = 1
              if y-m >= 0 and x+m <= N-1:
                  table[y-m][x+m] = 1
              if y+m <= N-1 and x-m >= 0:
                  table[y+m][x-m] = 1
              if y-m >= 0 and x-m >= 0:
                  table[y-m][x-m] = 1
          return True
      else:
          return False
  start=time.perf_counter()
  table = [[0]*N for _ in range(N)]
  temp = []
  for i in range(N):
    temp.append(i)    
  perms = permutations(temp)


  num_comb = 0

  for perm in perms:
      if put_queen(perm[0], 0) == True :
          if N==1:
  #          print_table()
            num_comb += 1
  #          print(f"solution{num_comb}")
  #          print(" ")
          elif N>1:
            if put_queen(perm[1], 1) == True :
              if N==2:
  #              print_table()
                num_comb += 1
  #              print(f"solution{num_comb}")
  #              print(" ")
              elif N>2: 
                if put_queen(perm[2], 2) == True:
                  if N==3:
  #                  print_table()
                    num_comb += 1
  #                  print(f"solution{num_comb}")
  #                  print(" ")
                  elif N>3:
                    if put_queen(perm[3], 3) == True:
                      if N==4:
  #                      print_table()
                        num_comb += 1
  #                      print(f"solution{num_comb}")
  #                      print(" ")
                      elif N>4 :
                        if put_queen(perm[4], 4) == True:
                          if N==5:
  #                         print_table()
                            num_comb += 1
  #                          print(f"solution{num_comb}")
  #                          print(" ")
                          elif N>5:
                            if put_queen(perm[5], 5) == True:
                              if N==6:
  #                              print_table()
                                num_comb += 1
  #                              print(f"solution{num_comb}")
  #                              print(" ")
                              elif N>6:
                                if put_queen(perm[6], 6) == True:
                                  if N==7 :
  #                                  print_table()
                                    num_comb += 1
  #                                  print(f"solution{num_comb}")
  #                                  print(" ")
                                  elif N>7:
                                    if put_queen(perm[7], 7) == True:
                                      if N==8 :
  #                                     print_table()
                                        num_comb += 1
  #                                      print(f"solution{num_comb}")
  #                                      print(" ")
                                      elif N>8:
                                        if put_queen(perm[8], 8) == True:
                                          if N==9 :
  #                                          print_table()
                                            num_comb += 1
  #                                          print(f"solution{num_comb}")
  #                                          print(" ")
                                          elif N>9:
                                            if put_queen(perm[9], 9) == True:
                                              if N==10 :
  #                                              print_table()
                                                num_comb += 1
  #                                              print(f"solution{num_comb}")
  #                                              print(" ")
      table = [[0] * N for _ in range(N)]
  stop=time.perf_counter()
  print("N = {}".format(N))
  print("time = {}".format(stop-start))

print("Recursion")
for i in range(7):
    N = i+4			 # N x N Board 
    numSol = 0  			# number of solutions

    b = N*[-1]  			# indices = rows, b[index] = coloumn, first init to -1
    colFree = N*[1] 			# all N col are free at first
    upFree = (2*N - 1)*[1] 		# all up diagonals are free at first
    downFree = (2*N - 1)*[1]    		# all down diagonals are free at first

    def printBoard(b):
        print(b)

    def putQueen(r, b, colFree, upFree, downFree):
        global N
        global numSol
        for c in range(N): # ใล่ใส่ไปทีละ column ทุก col.
            if colFree[c] and upFree[r+c] and downFree[r-c+N-1]: #ใส่ได้?
                b[r] = c    # ใส่ ที่ r, c

                colFree[c] = upFree[r+c] = downFree[r-c+N-1] = 0 # เปลี่ยน data struct ไม่ให้ใส่แนวนี้

                if r == N-1:       # ถ้าใส่ควีนครบแล้ว
                    #printBoard(b)  #print(b)
                    numSol += 1
                else:
                    putQueen(r+1, b, colFree, upFree, downFree)  # ใส่ควีนแถวถัดไป
                colFree[c] = upFree[r+c] = downFree[r-c+N-1] = 1 #เอา Queen ออกเพื่อให้ได้ solution อื่น
                                                                # หรือ เพราะ queen ตัวนี้แม้ใส่ได้แต่ไม่ทำให้เกิด solution
    start=time.perf_counter()
    putQueen(0, b, colFree, upFree, downFree)   #  first add at 1st  (ie. row 0)
    #print('number of solutions = ', numSol)
    stop=time.perf_counter()
    print("N = {}".format(N))
    print("time = {}".format(stop-start))