def gcd(a,b):
    divisor = min(a,b)
    dividend = max(a,b)
    if(dividend % divisor == 0):
        return divisor
    
    r = dividend % divisor
    return gcd(r,divisor)

nlist = [] # this stores all thenumbers given as input
print("Enter the five numbers")
product = 1
for i in range(5):
    nlist.append(int(input()))

hcf = gcd(nlist[0],nlist[1])
for i in range(3):
    hcf = gcd(hcf,nlist[2+i])

print("GCD = {0}".format(hcf))

