def inputmatrix():
    print("Please enter the elements row wise, separated by spaces")
    matrix=input().split()
    return(matrix)

def transpose(matrix):
    trans=[]
    for i in range(0,3):
        for j in range(0,3):
            trans.append(matrix[i+3*j])
    return(trans)
def val(frac):
    numrdenom=frac.split('/')
    return(int(numrdenom[0])/int(numrdenom[1]))

def trace(matrix):
    sum=0
    for i in range(0,3):
        sum=sum+val(matrix[i+3*i])
    return(sum)

mat=inputmatrix()
print(mat)
print(transpose(mat))
print(trace(mat))


