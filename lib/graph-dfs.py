def dfs(k):
    Mark[k] = 1
    print("Now in ", (k+1))
    for j in range(len(a)):
        if a[k][j] == 1 and Mark[j] == 0:
            #print(a[k][j] == 1, " and ", Mark[j] == 0, " = ", a[k][j] == 1 and Mark[j] == 0)
            #print(Mark)
            dfs(j)
    return

a = [[0, 1, 1, 1, 0, 0, 0, 0, 0, 0],	
     [1, 0, 0, 0, 1, 1, 0, 0, 0, 0], 
     [1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
     [1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
     [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
     [0, 0, 1, 0, 0, 1, 0, 1, 0, 0],
     [0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
     [0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]

Mark = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

while True:
    
    i = int(input("Give start node (1-%d) or out of range to exit: " % (len(a))))
    if i >= 1 and i <= len(a):
        for m in range(len(a)):
            Mark[m] = 0
        dfs(i-1)
    else:
        break