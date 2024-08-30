def binary_search(list,start,end,key):
    si = start
    ei = end
    while(si <= ei):
        mid = (si+ei)//2
        if(key < list[mid]):
            ei = mid-1
        elif(key > list[mid]):
            si = mid+1
        else:
            return mid
    return -1 #element not found

def remove(list,value):
    
    for i in range(len(list)):
        if(list[i] == value):
            break

    while(list[i] == value):
        list.pop(i)
        if(len(list) == 0 | i == len(list)):
            return

nList = []
print("Enter the numbers, press A to stop")
x = 0
while(True):
    x = input()
    if(x == "a"):
        break
    nList.append(int(x))
target = int(input("Enter the target value "))

nList.sort()
#print(nList) # this is the sorted list

outList = []
while(len(nList) > 0):
    c = nList[0]
    x = binary_search(nList,1,len(nList)-1,target-c)
    remove(nList,c)
    
    if(x != -1):
        outList.append((c,target-c))
        remove(nList,target-c)

print("The required list is as follows :-")
print(outList)



