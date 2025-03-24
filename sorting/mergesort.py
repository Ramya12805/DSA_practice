def merge_sort(arr):
    if len(arr)<=1:
        return arr
    
    mid=len(arr)//2
    left_half=arr[:mid]
    right_half=arr[mid:]
    left_half=merge_sort(left_half)
    right_half=merge_sort(right_half)
    return merge(left_half,right_half)
def merge(left,right):
    res=[]
    li=ri=0
    while li<len(left) and ri<len(right):
        if left[li]<right[ri]:
            res.append(left[li])
            li+=1
        else:
            res.append(right[ri])
            ri+=1
    res.extend(left[li:])
    res.extend(right[ri:])
    return res

arr=[5,2,3,1,6]
k=merge_sort(arr)
print(k)
