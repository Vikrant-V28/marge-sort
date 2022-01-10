''' Marge Sort is Merge Sort is dividing the list in half over and over again until each piece is only one item long. Then those items are put back together (merged) in sort-order.
To implement the algorithm, we will need a merge function, that will join the two parts of the list together in sorted order. So, here we are taking the list, divide it into two sections, 
and continue this process until each element become a single item. Then we start to merge them back together to get back the sorted items.'''

def merge(left, right):
    if not len(left) or not len(right):
        return left or right
    
    result = []
    i, j = 0, 0

    while (len(result) < len(left) + len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i+= 1
        else:
            result.append(right[j])
            j+= 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break
      
    return result

def merge_sort(list):
    if len(list) < 2:
        return list
  
    mid = len(list)//2
    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])

    return merge(left, right)


a = [3,4,6,5,8,2,9,1,7]
print(merge_sort(a))


''' Bubble Sort is used to sort a list of elements, by comparing two adjacent elements and swapping them,if they are not in order.'''

def BubbleSort(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        for j in range(passnum):
            if nlist[j] > nlist[j+1]:
                nlist[j], nlist[j+1] = nlist[j+1], nlist[j]

nlist = [14,46,43,27,57,41,52,98,64,9,28]
BubbleSort(nlist)
print(nlist)