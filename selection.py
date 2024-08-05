def selectionsort(list):
    for idx in range(len(list)):
        min_id=idx
        for j in range(idx+1,len(list)):
            if list[min_id]>list[j]:
                min_id=j
        list[idx],list[min_id]=list[min_id],list[idx]
l=[22,13,4,8,17,26,53,4] 
selectionsort(l)
print(l)               
    