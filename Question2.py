
def iterate(a2d,x,y,n,val):
    v = val
    i= 1 
    j = 0 
    while(j < n):
        a2d[x][y+j] = v
        v += 1
        j += 1
    j = n-2

    while(i < n):
        a2d[x+i][y+n-1] = v
        v += 1
        i += 1
    i = n-2

    while(j >= 0):
        a2d[x+n-1][y+j] = v
        v += 1
        j -= 1

    while(i >= 1):
       a2d[x+i][y] = v
       v += 1
       i -= 1 
    return v

def display(a2d,n):
    for i in range(n):
        for j in range(n):
            print(a2d[i][j],end = " ")
        print() 

n = int(input("Enter the number \n"))
array_2d = [[0 for i in range(n)] for j in range(n)]

s = 0 #this is the starting index
d = n #this is the starting dimension

x = 1 # x is the starting value
num = 0 # number of iterations

while( d > 0):
    c = iterate(array_2d,s,s,d,x)
    s += 1
    d -= 2
    x = c

iterate(array_2d,0,0,n,1)
print("The output is as follows")
display(array_2d,n)       
    
