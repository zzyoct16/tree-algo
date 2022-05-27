heap=input()
while (heap):
    result="Yes"
    heap=[int(index)for index in heap.split()]
    
    for index in range (len(heap)-1,0,-1):
        if heap[index] > heap[(index-1)//2]:
            result="No"
            break
    print(result)
    try:
        heap=input()
    except:
        break
