def bubblesort(l):
    n=int(len(l))
    for i in range(n-1):
        for j in range(n-i-1):
            if l[j]>l[j+1]:
                l[j], l[j+1]=l[j+1], l[j]


def selectionsort(l):
    n=int(len(l))
    for i in range(n-1):
        k=i
        for j in range(i,n):
            if l[k]>l[j]:
                k=j
        l[k], l[i] = l[i], l[k]
        
def insertionsort(l):
    n=int(len(l))
    for i in range(n):
        for j in range(i,0,-1): 
            if l[i] < l[j]:
                l[i], l[j] = l[j], l[i]
                

x = [-2, 45, 0, 11, -9]
bubblesort(x)
print(x)
selectionsort(x)
print(x)
selectionsort(x)

print(x)