#your code in python
newarr = [1,2,3,4,5,6,7,8,9,10]
rotate_times = int(input("How many times do you want to rotate array?: "))

for i in range(rotate_times):
    temp = newarr[0]
    for j in range(newarr.__len__()-1):
        newarr[j] = newarr[j+1]
    newarr[newarr.__len__()-1] = temp
print(newarr)
#test
#testgit
