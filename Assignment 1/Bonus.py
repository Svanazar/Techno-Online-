n=int(input())
# def test(x,y):
#     if(x>=y):
#         return("YES")
#     if(x%2!=0):
#         x=x-1
#     while(x>1):
#         z=x
#         while(True):
#             if(z%2==0):
#                 z=1.5*z
#             if(z>=y):
#                 return("YES")
#             if(z%2!=0):
#                 z=z-1
#         x=x-2
#     return("NO")
def bettertest(x,y):
    if(x>3):
        return("YES")
    if(x>=y):
        return("YES")
    if((x==2) and (y==3)):
        return("YES")
    return("NO")
cases=[]
for i in range(n):
    cases.append(input().split())
# for case in cases:
#     x=int(case[0])
#     y=int(case[1])
#     print(test(x,y))
for case in cases:
    x=int(case[0])
    y=int(case[1])
    print(bettertest(x,y))

   

