r = int(input("Enter number of Rows:"))
c = int(input("Enter number of Columns:"))
Matrix=[]

for i in range(r):
    Inputs=list(map(float,input().split()))
    if len(Inputs) == c:
        Matrix.append(Inputs)
    else:
        print("Input Overload !!!!")
        break

Rows=0
Columns=0

def Matrix_Operations(j,k):
    a=Matrix[j][k]
    for i1 in range(len(Matrix[j])):
        Matrix[j][i1]=Matrix[j][i1]/a
    for i2 in range(r):
        if i2==j:
            continue
        else:
            b=Matrix[i2][k]
            for i3 in range(len(Matrix[0])):
                Matrix[i2][i3]=Matrix[i2][i3]-(Matrix[j][i3]*b)
    return Matrix

def Row_Swap(j,k):
    for i in range(j+1,len(Matrix)):
        if Matrix[i][k]==1:
                Matrix[i],Matrix[j]=Matrix[j],Matrix[i]
    return Matrix

print(" ")
while True:
    if Rows<len(Matrix) and Columns<=len(Matrix[0])-1:
        if Matrix[Rows][Columns]==0:
            t=False
            for i in range(Rows+1,r):
                if Matrix[i][Columns]!=0:
                    Matrix[i],Matrix[Rows]=Matrix[Rows],Matrix[i]
                    Matrix=Matrix_Operations(Rows,Columns)
                    Rows+=1
                    Columns+=1
                    t=True
                    break
            if t==False:
                Columns+=1
        else:
            Row_Swap(Rows,Columns)
            Matrix_Operations(Rows,Columns)
            Rows+=1
            Columns+=1
    else:
        break

print("RREF of the Matrix:")
for i in range(len(Matrix)):
    for j in range(len(Matrix[0])):
        Matrix[i][j]=round(Matrix[i][j],3)
    print(*Matrix[i])

print(" ")
print("General Solution:")
l=[]
for i in range(len(Matrix[0])):
    count=0
    for y in range(len(Matrix)):
        count=count+Matrix[y][i]
    if count!=1:
        l.append(i)
l1=[]
l2=[]
for y in range(len(Matrix)):
    l3=[]
    for p in range(len(Matrix[0])):
        if p not in l and Matrix[y][p]==1:
            l1.append(p)
    for p in range(len(Matrix[0])):
        if p in l:
            l3.append([p,Matrix[y][p]])
    l2.append(l3)

L=[]
a=""
for i in range(len(Matrix[0])):
    if i in l:
        a+=("+"+'x'+str(i+1)+"*")
        for j in range(len(Matrix[0])):
            if j==i:
                L.append(1)
            if j!=i and j in l:
                L.append(0)
            if j not in l:
                for k in range(len(l1)):
                    if j==l1[k]:
                        for m in range(len(l2[k])):
                            if l2[k][m][0]==i:
                                L.append(-1*(l2[k][m][1]))
        a+=str(L)
        L=[]
print(a.lstrip("+"))
if a=="":
    print("The set of equations have trivial solutions.")
print("")