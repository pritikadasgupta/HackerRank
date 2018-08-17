
def insertion_sort(m,l):
    for i in range(1, m):
        j = i-1
        key = l[i]
        compare = l[j]
        while (j >= 0) and (compare > key):
            l[j]=key
            l[j+1] = compare
            j -= 1
            if j >=0:
                compare = l[j]
    print(*l, sep=' ')


m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
insertion_sort(m,ar)
