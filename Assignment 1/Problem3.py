def OR(A):
    O=[]
    for array in A:
        result=array[0]|array[1]
        O.append(result)
    print(O)
    return(O)
def AND(A):
    O=[]
    for array in A:
        result=array[0]&array[1]
        O.append(result)
    print(O)
    return(O)
def comparer(O,D):
    sum=0
    for i in range(0,len(O)):
        if(O[i]==D[i]):
            sum=sum+i+1
    return(sum)
A=[]
for i in range(0,9):
    arr=input()
    A.append([int(arr[0]),int(arr[1])])
print(A)
print(comparer(OR(A),AND(A)))


