#print a matrix filled with consecutive numbers starting from one(1)
'''The first cell (0,0) must have the number 1.
The last cell (n,m) must have the value n x m (The largest number).
All others will be filled diagonally, left bottom to right top.'''

# --------------------------ANSWER--------------------------

#declare two variables for rows and columns of matrix

row=int(input("Enter the number of row of the matrix: "))
column=int(input("Enter the number of column of the matrix: "))

matrix=[]
matrix=[[0 for m in range(column)]for n in range(row)]
    
k=row*column

#printing a empty metrix 
print("EMPTY metrix elements are : ")
for i in matrix:
    for j in i:
        print(j,end=" ")
    print()

val=1 #val is variable used for filling first column of metrix 

# for filling values of metrix 

for i in range(0,row):
     for j in range(0,column):

        if i==0 and j==0:
            matrix[i][j]=1

        elif j==0 and i!=j:
            val=val+i
            matrix[i][j]=val
    
        elif i==(row-1) and j==(column-1):
            matrix[i][j]=k

        elif i==0:
             matrix[i][j]=j*row
        else:
            d=matrix[i][j-1]
            matrix[i][j]=d+row



# metrix  printing---

print("metrix elements are : ")
for i in matrix:
    for j in i:
        print(j,end=" ")
    print()







