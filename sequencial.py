def sadd(alist,item):
    pos=0
    found=False
    while pos<len(alist)and not found:
        if alist[pos]==item:
            found=True
        else:
            pos=pos+1
    return found            
testlist=[1,5,32,56,89,54]
print(sadd(testlist,32))