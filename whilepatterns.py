'''
rows=5
i=1
while i<=rows:
    j=1
    while j<=i:
        print((i*2-1),end=" ")
        j=j+1
    i=i+1
    print('')

1  
3 3  
5 5 5
7 7 7 7
9 9 9 9 9

rows = 5
for i in range(rows):
    for j in range(rows):
        if i == 0 or i == rows - 1 or j == rows-i-1: 
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

* * * * * 
      *   
    *
  *
* * * * *


rows = 5
for i in range(rows):
    for j in range(rows):
        if j == rows-i-1 or i == j-rows+rows:
            print('*', end=' ')
            
        else:
            print(' ', end=' ')
    print()


*       * 
  *   *   
    *
  *   *
*       *

rows = 5
i = 0
while i <= rows - 1:
    j = 0
    while j < i:
        # display space
        print('', end=' ')
        j += 1
    k = i
    while k <= rows - 1:
        print('*', end=' ')
        k += 1
    print()
    i += 1

i = rows - 1
while i >= 0:
    j = 0
    while j < i:
        print('', end=' ')
        j += 1
    k = i
    while k <= rows - 1:
        print('*', end=' ')
        k += 1
    print('')
    i -= 1

* * * * * 
 * * * * 
  * * * 
   * * 
    * 
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
'''

