def insertion_sort(x):
    n = len(x)
    for i in range(1, n):
        key_item = x[i]
        j = i - 1
        while j>=0 and x[j]>key_item:
            x[j+1] = x[j]
            j -= 1
        x[j+1] = key_item
    return x

xlist=[13,11,12,10,1,5,9,3,7,8,6,2,4,0]
print(insertion_sort(xlist))
