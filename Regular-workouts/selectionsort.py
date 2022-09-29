a=[12,64,25,22,11]
for i in range(len(a)):
    min_idx=i
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            min_idx=j
        a[i],a[min_idx]=a[min_idx],a[i]
    print(a[i])