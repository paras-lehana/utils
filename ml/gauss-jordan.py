import numpy as np

#matrix = np.array([[0,1,2],[1,2,1],[2,7,8]])
matrix = np.array([[1,1,1,3],[3,-2,1,2],[5,-3,2,4]])
n,p = np.shape(matrix)

print("\n\n-----------------\n\nMatrix A:\n")
print(matrix[:,:p-1])

def isREF(matrix):
  
  n,p = np.shape(matrix)
  lastZeroRow = n
  lastNonZeroRow = 0
  
  for rownum, row in enumerate(matrix):
    
    #Checking for (1): If the last non-zero row is above the first all-zero row.
    for ele in row:
      if(ele != 0):
        lastNonZeroRow = rownum
        break
      
    if(lastNonZeroRow != rownum):
      lastZeroRow = rownum
    
  if(lastZeroRow <= lastNonZeroRow):
    return -1;

  #Checking for (2): Current row's pivot should be located to the right of upper row's pivot.
  
  leadingColumnOfAboveRow = -1
  
  for row in matrix:
    for colnum, ele in enumerate(row):
      if(ele != 0):
        if(colnum <= leadingColumnOfAboveRow):
          return -2
        leadingColumnOfAboveRow = colnum
        break
       
  
  #Checking for (3): Each row's pivot should not have any non-zero entry below itself
  
  for rownum, row in enumerate(matrix):
      for colnum, ele in enumerate(row):
        if(ele != 0):
          if(np.any(matrix[rownum+1:,colnum])):
            return -3
          break
          
  return 1;
   
   
# matrixTest = np.array([[1,2,1],[0,1,2],[0,0,0]])
# print("\n\n-----------------\n\nMatrix Test:\n")
# print(matrixTest)
#print(isREF(matrixTest))


def isRREF(matrix):
  
  #Checking for (1): If the matrix in its Row Echelon Form.
  
  if(isREF(matrix) != 1):
    return isREF(matrix)
  
  #Checking for (2): Each row's pivot should not have any non-zero entry above itself
  
  for rownum, row in enumerate(matrix):
      for colnum, ele in enumerate(row):
        if(ele != 0):
          if(np.any(matrix[:rownum,colnum])):
            return -4
          break
  
  #Checking for (3): Each row's pivot should be 1.
  
  for rownum, row in enumerate(matrix):
      for colnum, ele in enumerate(row):
        if(ele != 0):
          if(ele != 1):
            return -5
          break
  
  return 1


# matrixTest = np.array([[1,2,0,0],[0,0,1,0],[0,0,0,1],[0,0,0,0]])
# print("\n\n-----------------\n\nMatrix Test:\n")
# print(matrixTest)
# print(isRREF(matrixTest))

def pivot(column,ignoreIndex=0):
  for index, ele in enumerate(column[ignoreIndex:],start=ignoreIndex):
    if(ele != 0):
      return index, ele
  return -1, -1
  
  
swapRow = 0

n,p = np.shape(matrix)

for colnum, col in enumerate(matrix[:,:p-1].T):
  
  print("\n\n-----------------\n-----------------\nCurrent Column No.: ",colnum)
  
  if(isRREF(matrix[:,:p-1]) == 1):
    break
  
  print("\n\n-----------------\n\nCurrent Column:", col)
  
  pivotRow, pivotElement = pivot(col,swapRow)
  
  print("Pivot Element: ", pivotElement)
  
  matrix[[swapRow, pivotRow]] = matrix[[pivotRow, swapRow]]
  
  print("\n\n-----------------\n\nMatrix after Swapping Pivot Row:\n")
  print(matrix)
  
  if(pivotElement != 1):
    matrix[swapRow] = [ele/pivotElement for ele in matrix[swapRow]]
  
  print("\n\n-----------------\n\nMatrix after making Pivot Element 1:\n")
  print(matrix)
  
  for rownum, ele in enumerate(col[swapRow+1:],start=swapRow+1):
    if(ele != 0):
      matrix[rownum] = [rowEle-ele*matrix[swapRow,col] for col,rowEle in enumerate(matrix[rownum])]
      
      
  print("\n\n-----------------\n\nMatrix after making elements below Pivot Element 0:\n")
  print(matrix)
  
  swapRow = swapRow+1
  
  
print("\n\n-----------------\n\nMatrix after Row Echelon Form:\n")
print(matrix)

def ref(matrix):
  
  swapRow = 0

  for colnum, col in enumerate(matrix.T): #(5): swapRow keeps the count of ignored rows from start.

    if(isREF(matrix[:,:p-1]) == 1):
      break

    pivotRow, pivotElement = pivot(col,swapRow)
    matrix[[swapRow, pivotRow]] = matrix[[pivotRow, swapRow]] #(2): Swapping pivot row with the first row after ignored rows.

    if(pivotElement != 1):
      matrix[swapRow] = [ele/pivotElement for ele in matrix[swapRow]] #(3): Making each element of pivot row (after swapping) equal to one.

    for rownum, ele in enumerate(col[swapRow+1:],start=swapRow+1):
      if(ele != 0):
        matrix[rownum] = [rowEle-ele*matrix[swapRow,col] for col,rowEle in enumerate(matrix[rownum])] #(4): Making elements below in the column of pivot of current row equal to zero.

    swapRow = swapRow+1

    return matrix
  
for rownum in reversed(range(n)):
  print("\n\n-----------------\n-----------------\nCurrent Row No.: ", rownum)
  
  if(isRREF(matrix[:,:p-1]) == 1):
    break
    
  print("\n\n-----------------\n\nCurrent Row:", matrix[rownum,:])
  
  pivotColumn, pivotElement = pivot(matrix[rownum,:])
  
  print("Pivot Element: ", pivotElement)
  
  if(pivotColumn == -1 or rownum == 0):
    continue
    
  for upperRownum, ele in enumerate(matrix[:rownum,pivotColumn]):
    if(ele != 0):
      matrix[upperRownum] = [rowEle-ele*matrix[rownum,col] for col,rowEle in enumerate(matrix[upperRownum])]
      
  print("\n\n-----------------\n\nMatrix after making elements above Pivot Element 0:\n")
  print(matrix)
  
  
print("\n\n-----------------\n\nMatrix after Reduced Row Echelon Form:\n")
print(matrix)



def rref(matrix):
  matrix = ref(matrix[:,:p-1]) #(1): Convert to ref.
  
  for rownum in reversed(range(n)): #(4): Itering from last row, columns in order

    if(isRREF(matrix) == 1):
      break

    pivotColumn, pivotElement = pivot(matrix[rownum,:]) #(2): Calculating pivot element of current column

    print("Pivot Element: ", pivotElement)

    if(pivotColumn == -1 or rownum == 0): #In case pivot element is not found or we have reached to the first row
      continue

    for upperRownum, ele in enumerate(matrix[:rownum,pivotColumn]):
      if(ele != 0):
        matrix[upperRownum] = [rowEle-ele*matrix[rownum,col] for col,rowEle in enumerate(matrix[upperRownum])] #(3): Making elements above in the column of pivot of current row equal to zero.

    return matrix

for rownum in range(n):
  nosol = 0
  
  if(matrix[rownum,rownum] == 1):
    print(chr(ord('a')+rownum),': ',matrix[rownum,p-1])
  else:
    nosol = nosol + 1
    
if(nosol == n):
  print("\nInfinite Solutions")
elif(nosol != 0):
  print("\nNo Solution")
