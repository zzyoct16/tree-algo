def sort(heap,num):
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
heap=input()
while (heap):
    hea=heap.split()
    heap=[]
    for index in hea:
        heap.append(int(index))
    for index in range((len(heap)-1-1)//2,-1,-1 ):
        num=index
        sort(heap,index)
    new_list=[]
    while(heap):
        heap[0],heap[-1]=heap[-1],heap[0]
        new_list.append(heap.pop())
        sort(heap,0)
    new_list.reverse()
    print(*new_list,"")
    try:
        heap=input()
    except:
        break

