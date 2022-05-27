heap=input()
while (heap):
    heap=[int(index)for index in heap.split()]
    for index1 in range((len(heap)-2)//2,-1,-1 ):
        num=index1
        while(num<=(len(heap)-2)//2):
            try:
                final=(num+1)*2-1 if heap[(num+1)*2-1] >=heap[(num+1)*2] else(num+1)*2
                    
            except:
                final=(num+1)*2-1
            if heap[num]<heap[final]:
                heap[num],heap[final]=heap[final],heap[num]
                num=final
            else:
                break
    print(*heap,"")
            
    try:
        heap=input()
    except:
        break
