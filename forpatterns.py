'''
rows=5
for i in range(rows):              
    for j in range(i):
        print(i,end=' ')
    print(' ')          

1  
2 2
3 3 3
4 4 4 4



rows =  7
for i in range(1, rows + 1):
    for j in range(1,i+1):
        print(j, end=' ')
    print(' ')

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6
1 2 3 4 5 6 7



rows=5
b=0
for i in range(rows,0,-1):
    b+=1    
    for j in range(1,i+1):
        print(b,end=' ')
    print(' ')


1 1 1 1 1
2 2 2 2
3 3 3
4 4
5



rows=5
for i in range(rows,0,-1):
    for j in range(0,i+1):
        print(j,end=' ')
    print(' ')

0 1 2 3 4 5  
0 1 2 3 4  
0 1 2 3
0 1 2
0 1
'''


