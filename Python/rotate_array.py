import array

A = [1,2,3,4,5,6]
B = [9,382,1,4,5,6]

#rotating by using temp array
def rotate_by_x(Arr, sizeArr, x):
    tempArr = []
    for i in range(x):
        tempArr.append(Arr[i])
    for i in range(sizeArr-x):
        Arr[i] = Arr[x+i]
    for i in range(x):
        Arr[x+i] = tempArr[i]
    return Arr

#method by rotating x times
def rotate_by_m(Arr, sizeArr, m):
    for i in range(m-1):
        rotate(A,sizeArr)
    return Arr

def rotate(Arr,sizeArr):
    temp = Arr[0]
    for i in range(sizeArr - 1):
        Arr[i] = Arr[i + 1]
    Arr[sizeArr-1] = temp
    return Arr


#print(A)
#print(rotate_by_x(A,6,3))
#print(B)
#print(rotate(B,6))
